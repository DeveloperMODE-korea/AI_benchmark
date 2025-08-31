"""
Title: Poetica — A Tiny Weighted Grammar Expander (single file)
Purpose: Deterministic, elegant generation from a mini-DSL for context-free grammars.
Usage: python main.py [--seed SEED] [--start SYMBOL] [--max-steps N] [--max-tokens N]
                      [--format {text,json}] [--verbose] [--test]
Python: 3.11+

Overview
--------
Poetica compiles a compact grammar DSL (rules like `S -> NP VP | Name`, weights via `*k`)
and expands from a start symbol using a seeded PRNG. It produces either a polished text
string or a full JSON derivation tree. The core loop replaces the leftmost nonterminal
with a weighted alternative until only terminals remain (or a safety limit triggers).

Complexity
----------
Let m be the number of expansions and k the average #alternatives chosen among.
Time is O(m * k) for selection + O(total_symbols) for token maintenance; memory is
O(total_symbols) for the frontier + O(|G|) for the compiled rules. Safe limits bound
worst cases (left recursion, runaway growth) while keeping typical runs sub-second.
"""

from __future__ import annotations

import argparse
import json
import logging
import random
import re
import shlex
import sys
from dataclasses import dataclass
from typing import Dict, Iterable, List, Tuple, Union


# --------------------------- Defaults & Constants --------------------------- #

DEFAULT_SEED = 1
DEFAULT_START = "S"
DEFAULT_MAX_STEPS = 50
DEFAULT_MAX_TOKENS = 200

DEFAULT_GRAMMAR = r"""
# Poetica: a tiny grammar of "elegant English-ish" sentences.
# Nonterminals: UpperCamelCase. Terminals: anything else (quotes optional).
# Weights: add *k at the end of an alternative (e.g. `NP VP *2`).

S  -> NP VP .
NP -> Det N   | Det Adj N
VP -> V NP    | V Adv        | V
Det -> the | a
N   -> fox | dog | code | idea
Adj -> quick | elegant | careful
V   -> jumps | writes | tests | flows
Adv -> swiftly | beautifully | precisely
"""

NONTERM_RE = re.compile(r"^[A-Z][a-z]*([A-Z][a-z]*)*$")


# ------------------------------- Exceptions -------------------------------- #

class GrammarError(ValueError):
    """Grammar is invalid or references undefined symbols."""


class GenerationLimitError(RuntimeError):
    """Expansion stopped before all nonterminals could be resolved."""


# ------------------------------- Data Types -------------------------------- #

@dataclass(frozen=True)
class Production:
    """A single alternative of a rule."""
    symbols: Tuple[str, ...]
    weight: int = 1


@dataclass(frozen=True)
class Rule:
    """A rule: LHS -> alternatives (with weights)."""
    lhs: str
    alts: Tuple[Production, ...]


@dataclass
class Node:
    """Derivation node; terminals are plain strings, nonterminals are Node objects."""
    label: str
    children: List[Union["Node", str]] | None = None

    def to_dict(self) -> Dict:
        """Convert the derivation sub-tree to a plain dict."""
        if self.children is None:
            return {"label": self.label, "children": []}
        out = []
        for c in self.children:
            out.append(c.to_dict() if isinstance(c, Node) else {"terminal": c})
        return {"label": self.label, "children": out}


# ------------------------------ Core Utilities ----------------------------- #

def is_nonterminal(tok: str) -> bool:
    """Return True if token looks like a nonterminal (UpperCamelCase).

    >>> is_nonterminal("NP"), is_nonterminal("fox"), is_nonterminal(".")
    (True, False, False)
    """
    return bool(NONTERM_RE.match(tok))


def smart_join(tokens: Iterable[str]) -> str:
    """Join terminals with tidy spacing (no space before , . ; : ! ?).

    >>> smart_join(["hello", ",", "world", "!"])
    'hello, world!'
    """
    out: List[str] = []
    for t in tokens:
        if not out:
            out.append(t)
            continue
        if t in {",", ".", ";", ":", "!", "?"}:
            out[-1] = out[-1] + t
        elif t in {"'s"}:
            out[-1] = out[-1] + t
        else:
            out.append(" " + t)
    return "".join(out)


def _parse_weight(tokens: List[str]) -> tuple[List[str], int]:
    """Extract trailing *k weight; default 1."""
    if tokens and tokens[-1].startswith("*"):
        try:
            w = int(tokens[-1][1:])
            if w <= 0:
                raise ValueError
        except ValueError as e:
            raise GrammarError(f"Invalid weight token: {tokens[-1]!r}") from e
        return tokens[:-1], w
    return tokens, 1


def parse_grammar(text: str) -> Dict[str, Rule]:
    """Compile DSL into a mapping {lhs: Rule}.

    Syntax:
      LHS -> alt1 | alt2 *3 | sym "quoted terminal" punctuation
    Notes:
      - Nonterminals: UpperCamelCase; everything else is terminal.
      - Weights via trailing `*k` on an alternative (k>=1).
      - Lines starting with '#' are comments.

    >>> g = parse_grammar("S -> hello world")
    >>> sorted(g["S"].alts[0].symbols)
    ['hello', 'world']
    """
    rules: Dict[str, List[Production]] = {}
    for raw in text.splitlines():
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        if "->" not in line:
            raise GrammarError(f"Missing '->' in rule: {line}")
        lhs, rhs = map(str.strip, line.split("->", 1))
        if not is_nonterminal(lhs):
            raise GrammarError(f"LHS must be Nonterminal (UpperCamelCase): {lhs}")
        alts: List[Production] = rules.setdefault(lhs, [])
        for alt in rhs.split("|"):
            toks = shlex.split(alt.strip())
            toks, w = _parse_weight(toks)
            if not toks:
                raise GrammarError(f"Empty alternative in: {line}")
            alts.append(Production(tuple(toks), w))
    # Freeze rules
    frozen: Dict[str, Rule] = {k: Rule(k, tuple(v)) for k, v in rules.items()}
    # Undefined refs check
    defined = set(frozen.keys())
    referenced = {
        tok for r in frozen.values() for p in r.alts for tok in p.symbols if is_nonterminal(tok)
    }
    undefined = referenced - defined
    if undefined:
        raise GrammarError(f"Undefined nonterminals: {', '.join(sorted(undefined))}")
    return frozen


def _weighted_choice(rng: random.Random, alts: Tuple[Production, ...]) -> Production:
    total = sum(a.weight for a in alts)
    r = rng.randrange(total)  # integer arithmetic avoids float quirks
    upto = 0
    for a in alts:
        upto += a.weight
        if r < upto:
            return a
    # Defensive (should be unreachable):
    return alts[-1]


def expand(
    grammar: Dict[str, Rule],
    *,
    start: str = DEFAULT_START,
    seed: int = DEFAULT_SEED,
    max_steps: int = DEFAULT_MAX_STEPS,
    max_tokens: int = DEFAULT_MAX_TOKENS,
    logger: logging.Logger | None = None,
) -> tuple[str, Node]:
    """Expand from `start` using weighted leftmost derivation.

    Raises:
        GenerationLimitError: if limits stop expansion prematurely.

    >>> g = parse_grammar("S -> hello world")
    >>> text, _ = expand(g, start="S", seed=7)
    >>> text
    'hello world'
    """
    if start not in grammar:
        raise GrammarError(f"Unknown start symbol: {start}")
    rng = random.Random(seed)
    tokens: List[str] = [start]
    root_node = Node(start)  # Create root node
    forest: List[Union[Node, str]] = [root_node]  # mirrors `tokens`

    steps = 0
    while True:
        if len(tokens) > max_tokens:
            raise GenerationLimitError("Token limit exceeded.")
        # Find leftmost nonterminal
        idx = next((i for i, t in enumerate(tokens) if is_nonterminal(t)), None)
        if idx is None:
            # Done
            terminals = [t for t in tokens if not is_nonterminal(t)]
            return smart_join(terminals), root_node
        if steps >= max_steps:
            raise GenerationLimitError("Step limit reached with nonterminals remaining.")
        nt = tokens[idx]
        rule = grammar.get(nt)
        if rule is None or not rule.alts:
            raise GrammarError(f"No productions for nonterminal: {nt}")

        prod = _weighted_choice(rng, rule.alts)
        if logger:
            logger.info("Expand %s -> %s", nt, " ".join(prod.symbols))

        # Build children slice
        child_elems: List[Union[Node, str]] = []
        for s in prod.symbols:
            child_elems.append(Node(s) if is_nonterminal(s) else s)

        # Patch tree and frontier
        node = forest[idx]
        assert isinstance(node, Node)
        node.children = child_elems
        tokens[idx : idx + 1] = list(prod.symbols)
        forest[idx : idx + 1] = child_elems
        steps += 1


# ------------------------------ CLI Entrypoint ------------------------------ #

def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        description="Poetica — Tiny weighted grammar expander (deterministic, single file).",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    p.add_argument("--seed", type=int, default=DEFAULT_SEED, help="Seed for reproducible generation.")
    p.add_argument("--start", type=str, default=DEFAULT_START, help="Start symbol.")
    p.add_argument("--max-steps", type=int, default=DEFAULT_MAX_STEPS, help="Expansion step limit.")
    p.add_argument("--max-tokens", type=int, default=DEFAULT_MAX_TOKENS, help="Frontier token limit.")
    p.add_argument("--format", choices={"text", "json"}, default="text", help="Output format.")
    p.add_argument("--verbose", action="store_true", help="Enable informative expansion logs.")
    p.add_argument("--grammar", type=str, default=None,
                   help="Inline grammar text; if omitted, uses the built-in DEFAULT_GRAMMAR.")
    p.add_argument("--test", action="store_true", help="Run doctests + unit tests and exit.")
    return p


def main(argv: List[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    if args.test:
        return run_tests()

    logger = logging.getLogger("poetica")
    if args.verbose:
        logging.basicConfig(level=logging.INFO, format="%(message)s")

    try:
        gtext = args.grammar if args.grammar else DEFAULT_GRAMMAR
        grammar = parse_grammar(gtext)
        text, tree = expand(
            grammar,
            start=args.start,
            seed=args.seed,
            max_steps=args.max_steps,
            max_tokens=args.max_tokens,
            logger=logger if args.verbose else None,
        )
    except (GrammarError, GenerationLimitError) as e:
        print(f"error: {e}", file=sys.stderr)
        return 2

    if args.format == "text":
        print(text)
    else:
        print(json.dumps({"text": text, "tree": tree.to_dict()}, ensure_ascii=False, indent=2))
    return 0


# --------------------------------- Testing --------------------------------- #

def run_tests() -> int:
    """Run doctests and a compact unittest suite (≤2s)."""
    import doctest
    import unittest

    class PoeticaTests(unittest.TestCase):
        def test_normal_generation(self) -> None:
            g = parse_grammar("S -> hello world")
            out, root = expand(g, start="S", seed=42)
            self.assertEqual(out, "hello world")
            self.assertEqual(root.label, "S")

        def test_undefined_symbol(self) -> None:
            with self.assertRaises(GrammarError):
                parse_grammar("S -> X")  # X undefined

        def test_limit_detection(self) -> None:
            g = parse_grammar("S -> S S")  # left recursion; needs a limit
            with self.assertRaises(GenerationLimitError):
                expand(g, start="S", seed=0, max_steps=5, max_tokens=20)

    # doctest
    failures, _ = doctest.testmod(optionflags=doctest.ELLIPSIS)
    # unittest
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(PoeticaTests)
    result = unittest.TextTestRunner(verbosity=0).run(suite)
    ok = (failures == 0) and result.wasSuccessful()
    print("Doctest:", "OK" if failures == 0 else "FAIL")
    print("Unittest:", "OK" if result.wasSuccessful() else "FAIL")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
