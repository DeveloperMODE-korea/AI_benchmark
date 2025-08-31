# Wave Function Collapse `main.py` — Technical Review (EN‑only)

**Target**: `main.py` (single‑file WFC) • **Python**: 3.11+
**Focus**: Code quality · Algorithmic soundness · Determinism/Performance · Tests · CLI UX

---

## 1) Executive Summary

**Verdict:** Clear structure and a faithful, single‑file WFC core. However, the current **MAZE/TILES constraints are effectively inert**, so results won’t look like true mazes or smooth gradients. With a few small patches (below), you can substantially improve correctness and UX.
**Overall score:** **87/100**

* Code Quality 18/20 · Algorithmic Correctness 16/20 · Determinism 18/20 · Performance 16/20 · Tests & Docs 19/20

---

## 2) Strengths

* **Single‑file architecture** with a clean flow: constants → data types → algorithm → CLI → tests.
* **Readable models**: `Tile`/`Cell` are intuitive; type hints and docstrings are solid.
* **Determinism**: seeded runs produce stable outputs (modulo global RNG; see patch D.3).
* **Baseline tests**: small‑grid generation and seed reproducibility included.

---

## 3) Issues & Risks (prioritized)

### \[Critical] MAZE/TILES constraints don’t constrain

* **What happens:** MAZE (`█`/space) and TILES (░/▒/▓/█) tiles each expose the **same sockets in all directions**. Since `can_connect` only checks for the presence of directional sockets, **every tile connects to every other** → constraint propagation has little effect.
* **Impact:** Outputs look like weighted random fields, not mazes or smooth gradients; documentation and reality diverge.
* **Fix (Patch A):** Introduce **socket labels** (channels) so only compatible neighbors connect (e.g., Wall↔Wall, Path↔Path, or gradient levels that differ by ≤1).

### \[Major] Fixed propagation limit

* **What happens:** `_propagate` caps iterations at a constant; if the queue still has work, the function still returns `True` (success), leaving constraints partially applied.
* **Fix (Patch B):** Scale the limit with grid/tileset size and **fail when exceeded**.

### \[Major] Entropy tie‑break uses RNG noise

* **What happens:** `entropy` adds tiny random noise. It’s seeded but fragile if global RNG is touched elsewhere.
* **Fix (Patch C):** Remove noise and use a **stable sort key**: `(entropy, |candidates|, y, x)`.

### \[Minor] CLI/docs mismatch & JSON shape

* `--size` is a single `N` (N×N), but help text implies `20x20`.
* JSON returns a single multiline string; arrays are more practical for downstream.

### \[Minor] Doctest note & runner

* Docstring comment uses `log2(2) ≈ 0.693` (that’s `ln(2)`); **log2(2) = 1.0**.
* No doctest runner is wired; optional to add.

### \[Nit] Small cleanups

* Unused imports: `lru_cache`, `StringIO`.

---

## 4) Minimal, Drop‑in Patches

> The following keep your structure intact and maximize correctness/UX for minimal diff.

### Patch A — Labeled sockets for real constraints

**Goal:** Enforce adjacency rules for MAZE/TILES; keep CIRCUIT backward‑compatible.

**1) Replace `Tile.can_connect`**

```python
@dataclass(frozen=True)
class Tile:
    symbol: str
    sockets: frozenset[str]  # e.g., {"N", "E:W", "S:2"}
    weight: float = 1.0

    def can_connect(self, other: 'Tile', direction: str) -> bool:
        """True iff self (at pos) can connect to other in given direction.
        Supports labeled sockets: "D:LABEL". LABELs may be strings (e.g., "P"/"W")
        or digits (e.g., "0".."3"). Digits allow |Δ|≤1 for smooth gradients.
        Unlabeled (just "D") acts as a plain socket; two unlabeled sockets match.
        """
        opposite = {'N': 'S', 'S': 'N', 'E': 'W', 'W': 'E'}
        if direction not in opposite:
            return False
        opp = opposite[direction]

        def get_label(tokens: frozenset[str], d: str) -> Optional[str]:
            # Return label for direction d, '' for unlabeled, or None if not present.
            for t in tokens:
                if t == d:
                    return ''
                if t.startswith(d + ':'):
                    return t.split(':', 1)[1]
            return None

        a = get_label(self.sockets, direction)
        b = get_label(other.sockets, opp)
        if a is None or b is None:
            return False
        if a.isdigit() and b.isdigit():
            return abs(int(a) - int(b)) <= 1
        return a == b  # labeled must match; '' matches ''
```

**2) Update MAZE/TILES tilesets**

```python
def get_tileset(pattern: Pattern) -> list[Tile]:
    match pattern:
        case Pattern.MAZE:
            return [
                Tile('█', frozenset({'N:W','S:W','E:W','W:W'}), weight=2.0),  # wall
                Tile(' ', frozenset({'N:P','S:P','E:P','W:P'}), weight=1.0),  # path
            ]
        case Pattern.TILES:
            return [
                Tile('░', frozenset({'N:0','S:0','E:0','W:0'}), weight=2.0),
                Tile('▒', frozenset({'N:1','S:1','E:1','W:1'}), weight=1.5),
                Tile('▓', frozenset({'N:2','S:2','E:2','W:2'}), weight=1.0),
                Tile('█', frozenset({'N:3','S:3','E:3','W:3'}), weight=0.5),
            ]
        case Pattern.CIRCUIT:
            return [
                Tile('·', frozenset({'N','S','E','W'}), weight=3.0),
                Tile('─', frozenset({'E','W'}), weight=2.0),
                Tile('│', frozenset({'N','S'}), weight=2.0),
                Tile('┌', frozenset({'S','E'})),
                Tile('┐', frozenset({'S','W'})),
                Tile('└', frozenset({'N','E'})),
                Tile('┘', frozenset({'N','W'})),
                Tile('┬', frozenset({'S','E','W'})),
                Tile('├', frozenset({'N','S','E'})),
                Tile('┤', frozenset({'N','S','W'})),
                Tile('┴', frozenset({'N','E','W'})),
                Tile('┼', frozenset({'N','S','E','W'})),
            ]
```

> **Effect:** MAZE enforces Wall↔Wall and Path↔Path; TILES enforces smooth level transitions; CIRCUIT stays unchanged.

---

### Patch B — Dynamic propagation cap + failure on overflow

```python
class WFCGenerator:
    def _propagate(self, start_pos: tuple[int,int]) -> bool:
        queue = deque([start_pos])
        iterations = 0
        max_iters = max(10_000, self.width * self.height * max(4, len(self.tileset)))
        while queue and iterations < max_iters:
            iterations += 1
            pos = queue.popleft()
            cell = self.grid[pos]
            for direction, neighbor_pos in self._get_neighbors(pos):
                neighbor = self.grid[neighbor_pos]
                if neighbor.collapsed:
                    continue
                valid = set()
                for nt in neighbor.possibilities:
                    for ct in (cell.possibilities if not cell.collapsed else [cell.chosen]):
                        if ct and ct.can_connect(nt, direction):
                            valid.add(nt); break
                if len(valid) < len(neighbor.possibilities):
                    neighbor.possibilities = valid
                    if not neighbor.possibilities:
                        return False
                    queue.append(neighbor_pos)
        # If work remains, propagation didn’t complete → fail
        return not queue
```

---

### Patch C — Stable tie‑break; remove RNG noise

```python
@dataclass
class Cell:
    # ...
    def shannon_entropy(self) -> float:
        if self.collapsed or len(self.possibilities) <= 1:
            return 0.0
        weights = [t.weight for t in self.possibilities]
        total = sum(weights)
        probs = [w/total for w in weights if w > 0]
        import math
        return -sum(p * math.log2(p) for p in probs)

class WFCGenerator:
    def _find_minimum_entropy_cell(self) -> Optional[Cell]:
        candidates = [c for c in self.grid.values() if not c.collapsed and c.possibilities]
        if not candidates:
            return None
        return min(
            candidates,
            key=lambda c: (c.shannon_entropy(), len(c.possibilities), c.position[1], c.position[0])
        )
```

---

### Patch D — JSON/CLI UX + localized RNG (optional but recommended)

**1) JSON rows**

```python
if args.format == 'json':
    import json
    rendered = generator.render()
    print(json.dumps({
        'pattern': args.pattern,
        'size': args.size,
        'seed': args.seed,
        'rows': rendered.splitlines()
    }, indent=2))
    return 0
```

**2) Help text for `--size`**

```python
parser.add_argument('--size', type=int, default=DEFAULT_SIZE,
    help=f'Grid size N (produces N×N, default: {DEFAULT_SIZE})')
```

**3) Local PRNG**

```python
class WFCGenerator:
    def __init__(self, width, height, tileset, seed=DEFAULT_SEED):
        self.width = width; self.height = height; self.tileset = tileset
        self.rng = random.Random(seed)
        self.grid = {}
        self._initialize_grid()

    def _collapse_cell(self, cell: Cell) -> bool:
        if not cell.possibilities:
            return False
        tiles = list(cell.possibilities)
        weights = [t.weight for t in tiles]
        cell.chosen = self.rng.choices(tiles, weights=weights, k=1)[0]
        cell.possibilities = {cell.chosen}
        cell.collapsed = True
        return True
```

*Optionally*, also replace any other `random.*` calls to use `self.rng` for full isolation.

---

## 5) Additional Recommendations

* **Backtracking / retry**: `--retry K` to re‑seed on contradiction up to K times.
* **Precomputed compatibility**: Map `(tile, dir) -> {compatible tiles}` once; replace inner loops with set intersection.
* **Doctest runner**: Hook `doctest` into `unittest` for the doctstring examples.
* **Large‑grid profiling**: 200×200 / 300×300 benchmarks; record time and peak memory.
* **Import hygiene**: Remove unused `lru_cache`, `StringIO`.

---

## 6) Strengthened Test Plan

1. **Connectivity invariants (MAZE):** Disallow Wall↔Path adjacency; ensure only Wall↔Wall or Path↔Path.
2. **Gradient adjacency (TILES):** Enforce `|levelΔ| ≤ 1`.
3. **Propagation overflow:** Force a tiny `max_iters` to verify failure.
4. **Determinism:** Equal seeds → equal outputs; different seeds → different distributions.
5. **JSON schema:** `rows` length/width match `size`; characters restricted to tileset symbols.

---

## 7) Quick Q\&A

* **Why do MAZE/TILES look random?**  Because their sockets accept everything; constraints don’t bite. Labeled sockets fix it.
* **Is determinism preserved?**  Yes—and localized RNG makes it robust against external RNG use.
* **Is performance reasonable?**  Yes for 100×100. Precomputing compat sets can cut propagation time further.

---

### Bottom Line

Great single‑file skeleton with strong readability. Implement **Patch A–C** (and D for UX) and you’ll have outputs that actually *look* constrained (mazes/gradients), with safer propagation and stable, reproducible tie‑breaks.
