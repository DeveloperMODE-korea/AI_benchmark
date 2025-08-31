# Ultra-Enhanced Prompt (Python, Single-File Masterpiece — Pushing AI Creativity Beyond Limits)

**Objective**
Craft a *single-file* Python 3.11+ program that reads instantly as a masterwork of programming — clear, cohesive, elegant, and intellectually impressive. The solution must showcase **extreme AI creativity within strict engineering discipline**. The design must balance beauty and practicality: no gimmicks, only refined brilliance. Deliver the complete code and a concise, insightful explanation. The intent here is not only to produce working software, but also to create a living artifact that demonstrates what truly masterful Python looks like when boundaries are pushed responsibly. Think of this as the intersection of engineering discipline and artistic craftsmanship, written in code form.

---

## Hard Constraints

1. **Single file only.** Absolutely no external dependencies beyond the Python standard library. No hidden I/O, sockets, or unsafe imports. Portability must be guaranteed, meaning the code must run as-is without setup.
2. **Deterministic by default.** If randomness is used, expose a `--seed` CLI flag, with a default seed ensuring reproducible runs so two executions yield identical results unless explicitly changed.
3. **Self-contained tests.** Provide inline doctests or a compact `unittest` suite executable with `python main.py --test` under 2 seconds, allowing quick validation of correctness.
4. **CLI interface.** Must include `--help` and descriptive usage. Invalid inputs handled gracefully with friendly error messages. Use `argparse` for professionalism.
5. **Type hints & docstrings.** Every public class/function must include type hints and precise docstrings. Follow PEP 8 formatting rules and PEP 257 docstring conventions for consistency and readability.
6. **Performance clarity.** Document complexity of the core algorithm in clear terms. Readers should understand expected scaling. Must scale to modest inputs on commodity laptops without hidden performance traps.
7. **No over-engineering.** Use advanced features (dataclasses, generators, decorators, itertools, functools) only when they *truly improve clarity or performance*. Avoid using them for showmanship alone.
8. **Line discipline.** Target 150–300 LOC (excluding comments/tests). Each line must earn its place. No filler code, no bloated sections.
9. **Style uniformity.** Enforce consistent formatting, indentation, spacing, naming, and docstring patterns. The code should look like it was written by one thoughtful engineer from start to finish.

---

## Problem Shape (select or propose equivalent)

* **Elegant simulation** (event-driven micro-scheduler, boids-lite, cellular automaton with text/ASCII visualization).
* **Algorithmic transformation** (graph algorithms with invariants, minimal hashing toy, elegant lossless codec).
* **Declarative mini-DSL** (domain rules interpreter, composable query engine, pattern matcher).
* **Generative structure** (tiling generator, constraint grammar expander, recursive fractal composer).
* **Scheduling/packing puzzle** (bin-packing heuristic + proof of invariants, knapsack-lite with traceability).
* **Mathematical elegance** (number theory visualization, symmetry exploration, pattern generation that reveals structure).

The task must be **non-trivial but compact**, solvable beautifully within one file. It should require a clever design but remain understandable after a careful read-through.

---

## Design Requirements

* **Cohesive flow.** Structure must follow a disciplined top-to-bottom layout: constants → datatypes → core logic → CLI glue → tests. No scattered, out-of-place functions.
* **Naming discipline.** Descriptive, unambiguous, intention-revealing identifiers that make the reader nod in approval.
* **Function purity.** Favor pure functions where possible. Minimize side effects except where strictly necessary (e.g., CLI).
* **Advanced features (judicious):**

  * `@dataclass(frozen=True)` for immutable domain objects where appropriate.
  * Generators/iterators for streaming transformations, yielding clarity over memory-heavy collections.
  * Context managers to enforce boundaries or ensure state cleanup.
  * `functools.lru_cache` where caching makes complexity improvements explicit.
  * `match` statements where they significantly simplify branching logic.
* **Documentation density.**

  * Module docstring: 5–12 lines explaining purpose, usage, and algorithmic insight.
  * Functions/classes: 1–3 line docstrings with doctest snippets where suitable.
* **Error handling.** Early validation of inputs. Clear, domain-specific exceptions if they enhance clarity.
* **Optional logging.** Minimal, lightweight, and activated only with `--verbose`.
* **Formatting discipline.** Enforce consistent spacing, alignment, and logical grouping. No dead code, no commented-out clutter.
* **Readability first.** Even complex logic must remain digestible through careful decomposition and naming.

---

## Testing & Verification

* `--test` flag must execute doctests/unittest quickly and reliably.
* At least 3 representative tests: normal input, edge case, and deliberate error path.
* Inline sample fixtures (lists, graphs, small text) must be included. No reliance on external files.
* Doctests in docstrings should serve as both documentation and lightweight validation.
* Unit tests must confirm invariants, edge handling, and correctness.

---

## Performance & Complexity

* Annotate algorithm complexity in Big-O notation within code comments.
* If heuristic-based, document best, average, and worst-case scenarios.
* Run time for default input must be **≤1s** on a normal laptop.
* Explain why performance is acceptable given the problem domain.

---

## Output & UX

* Default output must be human-friendly text to stdout.
* Provide `--format json` option if structured data fits naturally.
* Example CLI run should feel polished and professional:

  * `python main.py --help` → clear, concise usage guide.
  * `python main.py --test` → fast confirmation of correctness.
  * Normal runs should produce elegant, readable output.

---

## Required Postscript (after the code)

After the code, include an **Explanation** (≤200 words) describing:

* Why the problem is elegant and non-trivial.
* How the design balances creativity with rigor.
* Which Python features improve clarity, readability, or performance.
* Why the file immediately feels “masterful” at first glance.
* How the solution could inspire others to adopt disciplined yet creative Python design.

---

## Scoring Rubric (AI Benchmark)

* **Clarity & Structure (30%)** — File flow, naming, docstrings, conciseness, and logical ordering.
* **Pythonic Excellence (25%)** — Idiomatic feature usage, leveraging the best of the standard library.
* **Algorithmic Soundness (20%)** — Correctness, performance, invariants, and proof of properties where possible.
* **Creativity in Restraint (15%)** — Fresh, surprising design that still respects engineering rigor.
* **Testing & Tooling (10%)** — Inline doctests, unit tests, reproducibility, and CLI polish.

---

## Guardrails (forbidden anti-patterns)

* Obscure metaprogramming/reflection hurting readability.
* Decorator/context-manager overuse when a simple function suffices.
* Hidden global state, mutable singletons, or reliance on side effects.
* Dense, cryptic one-liners that impress at first glance but confuse on inspection.
* Gratuitous micro-optimizations lacking justification.
* Over-commenting with redundant prose instead of meaningful annotation.
* Use of non-standard idioms that create barriers for readers.

---

## Submission Format

1. Full single Python file (code first).
2. Brief Explanation section (≤200 words).
3. Example CLI runs (help, test, normal execution).
4. Optional: Annotated sample outputs or screenshots (if text-based visualization).

---

### Starter Header (optional for AI to emit)

```python
"""
Title: <Concise Program Name>
Purpose: <One-sentence description>
Usage: python main.py [--seed SEED] [--format {text,json}] [--test] [--verbose]
Python: 3.11+
"""
```

> The output must be a compact, rigorous, undeniably polished single file — the kind of artifact that compels respect the moment it is opened. It should stand as both a practical tool and a demonstration of disciplined creativity, setting the bar for what Python craftsmanship should look like when boundaries are pushed responsibly.

