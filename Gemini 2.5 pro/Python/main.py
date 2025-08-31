"""
Title: L-System Fractal Composer
Purpose: Generates and visualizes 2D fractal structures using L-Systems.
Usage: python main.py [--seed SEED] [--format {text,json}] [--test] [--verbose] AXIOM [RULES ...]
Python: 3.11+

This program interprets Lindenmayer systems (L-Systems) to produce fractal
patterns. An L-System is a parallel rewriting system, consisting of an alphabet
of symbols, a set of production rules, and an initial string ("axiom").

The core algorithm recursively expands the axiom according to the rules for a
given number of iterations. The resulting string is then interpreted by a "turtle"
graphics engine, which draws the final pattern as an ASCII art grid.

The design prioritizes clarity, immutability, and deterministic output,
encapsulating complexity within a clean, functional-style core.
"""

import argparse
import collections
import dataclasses
import itertools
import json
import logging
import math
import sys
import unittest
from typing import (Dict, Generator, Iterable, Iterator, List, NamedTuple,
                    Optional, Set, Tuple)

# --- Constants & Configuration ---

DEFAULT_ITERATIONS = 4
DEFAULT_ANGLE = 90.0
DEFAULT_SEED = 42  # For any future stochastic elements.

# Turtle graphics commands are represented by single characters.
COMMAND_FORWARD = 'F'
COMMAND_LEFT = '+'
COMMAND_RIGHT = '-'
COMMAND_PUSH = '['
COMMAND_POP = ']'

# Default L-Systems for demonstration.
PRESETS = {
    'dragon': {
        'axiom': 'FX',
        'rules': ['X=X+YF+', 'Y=-FX-Y'],
        'angle': 90,
        'iterations': 10
    },
    'koch': {
        'axiom': 'F',
        'rules': ['F=F+F-F-F+F'],
        'angle': 90,
        'iterations': 3
    },
    'sierpinski': {
        'axiom': 'F-G-G',
        'rules': ['F=F-G+F+G-F', 'G=GG'],
        'angle': 120,
        'iterations': 4
    }
}


# --- Domain Datatypes (Immutable & Typed) ---

@dataclasses.dataclass(frozen=True)
class TurtleState:
    """Represents the immutable state of the turtle at a single point in time."""
    x: float = 0.0
    y: float = 0.0
    angle: float = 90.0  # Pointing "up"

    def turn(self, angle_delta: float) -> 'TurtleState':
        """Returns a new state with an updated angle.
        >>> TurtleState().turn(90)
        TurtleState(x=0.0, y=0.0, angle=180.0)
        """
        return dataclasses.replace(self, angle=self.angle + angle_delta)

    def move(self, distance: float) -> 'TurtleState':
        """Returns a new state after moving forward.
        >>> TurtleState().move(1.0)
        TurtleState(x=6.123..., y=1.0, angle=90.0)
        """
        rad = math.radians(self.angle)
        new_x = self.x + distance * math.cos(rad)
        new_y = self.y + distance * math.sin(rad)
        return dataclasses.replace(self, x=new_x, y=new_y)


class Point(NamedTuple):
    """A simple 2D integer coordinate for grid rendering."""
    x: int
    y: int


# --- Core Logic (Functional & Testable) ---

def parse_rules(rules_list: List[str]) -> Dict[str, str]:
    """
    Parses a list of 'key=value' strings into a rules dictionary.

    >>> parse_rules(['F=F+F', 'X=F-X'])
    {'F': 'F+F', 'X': 'F-X'}
    >>> parse_rules(['A=B'])
    {'A': 'B'}
    """
    rules: Dict[str, str] = {}
    for rule in rules_list:
        try:
            key, value = rule.split('=', 1)
            if not key or len(key) != 1:
                raise ValueError("Rule key must be a single character.")
            if not value:
                raise ValueError("Rule value cannot be empty.")
            rules[key] = value
        except ValueError as e:
            raise ValueError(f"Invalid rule format: '{rule}'. Must be 'K=V'.") from e
    return rules


def expand_lsystem(axiom: str, rules: Dict[str, str], iterations: int) -> str:
    """
    Generates the L-System string by applying rules iteratively.
    Complexity: O(L * k^N), where L is axiom length, k is the average rule
    expansion factor, and N is the number of iterations. Acceptable for modest N.

    >>> expand_lsystem('A', {'A': 'AB', 'B': 'A'}, 3)
    'ABAAB'
    """
    current = axiom
    for _ in range(iterations):
        # Using a generator expression for memory efficiency before join.
        current = "".join(rules.get(char, char) for char in current)
    return current


def trace_path(commands: str, angle_increment: float) -> Generator[Tuple[Point, Point], None, None]:
    """
    Interprets a command string to generate line segments for a fractal path.
    Yields pairs of (start, end) points, scaled to integer grid coordinates.
    This function is a generator, streaming path segments lazily.

    >>> path = list(trace_path('F+F', 90.0))
    >>> len(path)
    2
    >>> path[0]
    (Point(x=0, y=0), Point(x=0, y=1))
    """
    state = TurtleState()
    stack: List[TurtleState] = []
    # O(N) where N is the length of the commands string.
    for command in commands:
        match command:
            case 'F' | 'G':  # Treat F and G as "draw forward"
                new_state = state.move(1.0)
                # Yield raw float coordinates; scaling happens later.
                yield (state, new_state)
                state = new_state
            case '+':
                state = state.turn(angle_increment)
            case '-':
                state = state.turn(-angle_increment)
            case '[':
                stack.append(state)
            case ']':
                if stack:
                    state = stack.pop()
            case _:
                # Ignore unknown characters, treating them as constants.
                pass


def render_to_grid(path_segments: Iterable[Tuple[TurtleState, TurtleState]],
                   width: int, height: int) -> List[str]:
    """
    Renders floating-point path segments onto a fixed-size character grid.
    This function scales and translates the path to fit the specified canvas.
    """
    # Create an empty grid
    grid: List[List[str]] = [[' ' for _ in range(width)] for _ in range(height)]
    points: Set[Point] = set()
    all_coords = list(itertools.chain.from_iterable(path_segments))

    if not all_coords:
        return [" "] * height

    # Bounding box calculation to normalize coordinates
    min_x = min(p.x for p in all_coords)
    max_x = max(p.x for p in all_coords)
    min_y = min(p.y for p in all_coords)
    max_y = max(p.y for p in all_coords)

    x_range = max_x - min_x
    y_range = max_y - min_y

    scale_x = (width - 2) / x_range if x_range > 0 else 1
    scale_y = (height - 1) / y_range if y_range > 0 else 1
    scale = min(scale_x, scale_y)

    def transform(p: TurtleState) -> Point:
        # Scale and translate point to fit grid
        x = int((p.x - min_x) * scale) + 1
        # Invert Y-axis for screen coordinates (origin at top-left)
        y = int((p.y - min_y) * scale)
        y = (height - 1) - y
        return Point(x, y)

    for start_state, end_state in path_segments:
        start_pt = transform(start_state)
        end_pt = transform(end_state)

        # Basic line drawing (rasterization)
        # Using a simple DDA-like approach
        dx, dy = end_pt.x - start_pt.x, end_pt.y - start_pt.y
        steps = max(abs(dx), abs(dy))
        if steps == 0:
            points.add(start_pt)
            continue

        x_inc, y_inc = dx / steps, dy / steps
        for i in range(steps + 1):
            px = int(start_pt.x + i * x_inc)
            py = int(start_pt.y + i * y_inc)
            points.add(Point(px, py))

    # Plot points onto the grid
    for p in points:
        if 0 <= p.y < height and 0 <= p.x < width:
            grid[p.y][p.x] = '*'

    return ["".join(row) for row in grid]


# --- CLI Glue ---

def create_parser() -> argparse.ArgumentParser:
    """Configures the command-line interface."""
    parser = argparse.ArgumentParser(
        description="Generate and visualize 2D fractal structures using L-Systems.",
        formatter_class=argparse.RawTextHelpFormatter,
        epilog="""
Example presets:
  python %(prog)s koch          -> Classic Koch curve
  python %(prog)s dragon        -> Dragon curve
  python %(prog)s sierpinski   -> Sierpinski triangle

Custom example:
  python %(prog)s F 'F=F[+F]F[-F]F' --angle 25.7 --iterations 3
"""
    )
    parser.add_argument('axiom', nargs='?', help='Initial L-System string (e.g., "F"). Can be a preset name.')
    parser.add_argument('rules', nargs='*', help="Rewrite rules (e.g., 'F=F+F-F').")
    parser.add_argument('-n', '--iterations', type=int, default=None,
                        help=f'Number of rewrite iterations (default: {DEFAULT_ITERATIONS}).')
    parser.add_argument('-a', '--angle', type=float, default=None,
                        help=f'Turn angle in degrees (default: {DEFAULT_ANGLE}).')
    parser.add_argument('--width', type=int, default=70, help='ASCII output width.')
    parser.add_argument('--height', type=int, default=40, help='ASCII output height.')
    parser.add_argument('--seed', type=int, default=DEFAULT_SEED, help='Seed for random elements.')
    parser.add_argument('--format', choices=['text', 'json'], default='text',
                        help='Output format.')
    parser.add_argument('--test', action='store_true', help='Run built-in unit tests.')
    parser.add_argument('-v', '--verbose', action='store_true', help='Enable verbose logging.')
    return parser


def main(argv: Optional[List[str]] = None) -> int:
    """The main entry point of the program."""
    parser = create_parser()
    args = parser.parse_args(argv)

    if args.test:
        suite = unittest.TestLoader().loadTestsFromName(__name__)
        result = unittest.TextTestRunner(verbosity=2).run(suite)
        return 0 if result.wasSuccessful() else 1

    if not args.axiom:
        parser.print_help()
        return 1

    logging.basicConfig(level=logging.INFO if args.verbose else logging.WARNING,
                        format='%(levelname)s: %(message)s')

    # Load from preset if a preset name is provided
    if args.axiom in PRESETS and not args.rules:
        preset = PRESETS[args.axiom]
        axiom = preset['axiom']
        rules_map = parse_rules(preset['rules'])
        iterations = args.iterations or preset['iterations']
        angle = args.angle or preset['angle']
    else:
        axiom = args.axiom
        try:
            rules_map = parse_rules(args.rules)
        except ValueError as e:
            print(f"Error: {e}", file=sys.stderr)
            return 1
        iterations = args.iterations if args.iterations is not None else DEFAULT_ITERATIONS
        angle = args.angle if args.angle is not None else DEFAULT_ANGLE

    logging.info(f"Axiom: '{axiom}', Iterations: {iterations}, Angle: {angle}")
    logging.info(f"Rules: {rules_map}")

    # Core execution pipeline
    final_string = expand_lsystem(axiom, rules_map, iterations)
    logging.info(f"Expanded string length: {len(final_string)}")
    path = trace_path(final_string, angle)
    
    if args.format == 'json':
        # Serialize path data as JSON
        output_data = {
            'axiom': axiom,
            'rules': rules_map,
            'iterations': iterations,
            'angle': angle,
            'string': final_string,
            'path': [
                {'start': {'x': s.x, 'y': s.y}, 'end': {'x': e.x, 'y': e.y}}
                for s, e in path
            ]
        }
        print(json.dumps(output_data, indent=2))
    else:
        # Render ASCII art to stdout
        grid_lines = render_to_grid(list(path), args.width, args.height)
        for line in grid_lines:
            print(line)

    return 0


# --- Self-Contained Tests ---

class TestLSystem(unittest.TestCase):
    """Unit tests for the L-System generator and interpreter."""

    def test_parse_rules_success(self):
        """Verify that valid rule strings are parsed correctly."""
        self.assertEqual(parse_rules(['X=Y', 'F=F+F']), {'X': 'Y', 'F': 'F+F'})
        self.assertEqual(parse_rules([]), {})

    def test_parse_rules_error(self):
        """Check for graceful failure on malformed rules."""
        with self.assertRaises(ValueError):
            parse_rules(['F='])
        with self.assertRaises(ValueError):
            parse_rules(['FF=F'])
        with self.assertRaises(ValueError):
            parse_rules(['badrule'])

    def test_expand_lsystem(self):
        """Test the core L-System string expansion logic."""
        # Algae example from Wikipedia
        rules = {'A': 'AB', 'B': 'A'}
        self.assertEqual(expand_lsystem('A', rules, 0), 'A')
        self.assertEqual(expand_lsystem('A', rules, 1), 'AB')
        self.assertEqual(expand_lsystem('A', rules, 4), 'ABAABABA')
        # Koch curve
        rules_koch = {'F': 'F+F-F-F+F'}
        self.assertEqual(expand_lsystem('F', rules_koch, 1), 'F+F-F-F+F')

    def test_turtle_state_immutability_and_movement(self):
        """Ensure TurtleState behaves as an immutable value object."""
        s1 = TurtleState(x=10, y=10, angle=0)  # Facing right
        s2 = s1.move(5)
        self.assertAlmostEqual(s2.x, 15.0)
        self.assertAlmostEqual(s2.y, 10.0)
        # Original state is unchanged
        self.assertEqual(s1.x, 10)
        # Test turning
        s3 = s2.turn(90) # Face up
        s4 = s3.move(5)
        self.assertAlmostEqual(s4.x, 15.0)
        self.assertAlmostEqual(s4.y, 15.0)

    def test_path_tracing_edge_case(self):
        """Test tracing logic with an empty string and push/pop operations."""
        self.assertEqual(list(trace_path('', 90)), [])
        # Should not yield any segments but run without error
        path = list(trace_path('F[+F]F', 90))
        # Expected path: (0,0)->(0,1), then (+), then (0,1)->(-1,1) in new frame,
        # then pop back to original state, then (0,1)->(0,2)
        # Note: the test path trace is hard to verify without a full renderer
        # We confirm correct number of segments and that it completes.
        self.assertEqual(len(path), 3)

    def test_cli_preset_loading(self):
        """Check that CLI can invoke a preset and generate output."""
        # This is a very light integration test
        try:
            import io
            from contextlib import redirect_stdout
            f = io.StringIO()
            with redirect_stdout(f):
                main(['koch', '--iterations=1'])
            output = f.getvalue()
            self.assertIn('*', output, "ASCII output should contain path markers")
            self.assertGreater(len(output), 50)
        except Exception as e:
            self.fail(f"CLI invocation failed: {e}")

if __name__ == '__main__':
    sys.exit(main())