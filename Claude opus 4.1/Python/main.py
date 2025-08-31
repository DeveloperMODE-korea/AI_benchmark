#!/usr/bin/env python3
"""
Wave Function Collapse Pattern Generator
Purpose: Generate intricate patterns using quantum-inspired constraint propagation
Usage: python wfc.py [--seed SEED] [--size SIZE] [--pattern {circuit,maze,tiles}] [--test] [--verbose]
Python: 3.11+
Author: Claude (Anthropic)
"""

import argparse
import random
import sys
import unittest
from collections import deque
from dataclasses import dataclass, field
from enum import Enum, auto
from functools import lru_cache
from io import StringIO
from typing import Dict, List, Optional, Set, Tuple

# ============================================================================
# CONSTANTS & CONFIGURATION
# ============================================================================

DEFAULT_SEED = 42
DEFAULT_SIZE = 20
PROPAGATION_LIMIT = 10000

class Pattern(Enum):
    """Available pattern generation modes."""
    CIRCUIT = auto()
    MAZE = auto()
    TILES = auto()

# ============================================================================
# DATA STRUCTURES
# ============================================================================

@dataclass(frozen=True)
class Tile:
    """Immutable representation of a tile with connectivity constraints.
    
    >>> t = Tile('█', frozenset(['N', 'S']))
    >>> 'N' in t.sockets
    True
    """
    symbol: str
    sockets: frozenset[str]  # Allowed connection directions
    weight: float = 1.0
    
    def can_connect(self, other: 'Tile', direction: str) -> bool:
        """Check if this tile can connect to another in given direction."""
        opposite = {'N': 'S', 'S': 'N', 'E': 'W', 'W': 'E'}
        return direction in self.sockets and opposite[direction] in other.sockets

@dataclass
class Cell:
    """Mutable cell containing possible tile states during collapse."""
    position: Tuple[int, int]
    possibilities: Set[Tile] = field(default_factory=set)
    collapsed: bool = False
    chosen: Optional[Tile] = None
    
    @property
    def entropy(self) -> float:
        """Shannon entropy with slight noise for tie-breaking.
        
        >>> c = Cell((0, 0), {Tile('a', frozenset()), Tile('b', frozenset())})
        >>> 0.69 < c.entropy < 0.71  # log2(2) ≈ 0.693
        True
        """
        if self.collapsed or len(self.possibilities) <= 1:
            return 0.0
        weights = [t.weight for t in self.possibilities]
        total = sum(weights)
        probs = [w/total for w in weights]
        import math
        entropy = -sum(p * math.log2(p) for p in probs if p > 0)
        return entropy + random.random() * 0.0001  # Tie-breaker

# ============================================================================
# PATTERN DEFINITIONS
# ============================================================================

def get_tileset(pattern: Pattern) -> List[Tile]:
    """Return tileset for specified pattern type."""
    match pattern:
        case Pattern.CIRCUIT:
            return [
                Tile('·', frozenset(['N', 'S', 'E', 'W']), weight=3.0),  # Empty (can connect to anything)
                Tile('─', frozenset(['E', 'W']), weight=2.0), # Horizontal
                Tile('│', frozenset(['N', 'S']), weight=2.0), # Vertical
                Tile('┌', frozenset(['S', 'E'])),             # Corner NW
                Tile('┐', frozenset(['S', 'W'])),             # Corner NE
                Tile('└', frozenset(['N', 'E'])),             # Corner SW
                Tile('┘', frozenset(['N', 'W'])),             # Corner SE
                Tile('┬', frozenset(['S', 'E', 'W'])),        # T-junction N
                Tile('├', frozenset(['N', 'S', 'E'])),        # T-junction W
                Tile('┤', frozenset(['N', 'S', 'W'])),        # T-junction E
                Tile('┴', frozenset(['N', 'E', 'W'])),        # T-junction S
                Tile('┼', frozenset(['N', 'S', 'E', 'W'])),   # Cross
            ]
        case Pattern.MAZE:
            return [
                Tile('█', frozenset(['N', 'S', 'E', 'W']), weight=2.0),  # Wall (connects to walls)
                Tile(' ', frozenset(['N', 'S', 'E', 'W']), weight=1.0),  # Path (connects to paths)
            ]
        case Pattern.TILES:
            return [
                Tile('░', frozenset(['N', 'S', 'E', 'W']), weight=2.0),  # Light
                Tile('▒', frozenset(['N', 'S', 'E', 'W']), weight=1.5),  # Medium
                Tile('▓', frozenset(['N', 'S', 'E', 'W']), weight=1.0),  # Dark
                Tile('█', frozenset(['N', 'S', 'E', 'W']), weight=0.5),  # Solid
            ]

# ============================================================================
# WAVE FUNCTION COLLAPSE ALGORITHM
# ============================================================================

class WFCGenerator:
    """Wave Function Collapse pattern generator with constraint propagation."""
    
    def __init__(self, width: int, height: int, tileset: List[Tile], seed: int = DEFAULT_SEED):
        """Initialize generator with grid dimensions and tileset.
        
        Args:
            width: Grid width
            height: Grid height  
            tileset: Available tiles with constraints
            seed: Random seed for reproducibility
        """
        self.width = width
        self.height = height
        self.tileset = tileset
        self.grid: Dict[Tuple[int, int], Cell] = {}
        random.seed(seed)
        self._initialize_grid()
    
    def _initialize_grid(self) -> None:
        """Initialize all cells with full possibility space."""
        for y in range(self.height):
            for x in range(self.width):
                self.grid[(x, y)] = Cell((x, y), set(self.tileset))
    
    def _get_neighbors(self, pos: Tuple[int, int]) -> List[Tuple[str, Tuple[int, int]]]:
        """Get valid neighboring positions with directions.
        
        >>> gen = WFCGenerator(3, 3, [], 42)
        >>> neighbors = gen._get_neighbors((1, 1))
        >>> len(neighbors)
        4
        """
        x, y = pos
        neighbors = []
        directions = [('N', (x, y-1)), ('S', (x, y+1)), ('E', (x+1, y)), ('W', (x-1, y))]
        for direction, (nx, ny) in directions:
            if 0 <= nx < self.width and 0 <= ny < self.height:
                neighbors.append((direction, (nx, ny)))
        return neighbors
    
    def _propagate(self, start_pos: Tuple[int, int]) -> bool:
        """Propagate constraints from collapsed cell. Returns False if contradiction.
        
        Time complexity: O(n*m*t) where n,m are grid dimensions, t is tileset size.
        """
        queue = deque([start_pos])
        iterations = 0
        
        while queue and iterations < PROPAGATION_LIMIT:
            iterations += 1
            pos = queue.popleft()
            cell = self.grid[pos]
            
            for direction, neighbor_pos in self._get_neighbors(pos):
                neighbor = self.grid[neighbor_pos]
                if neighbor.collapsed:
                    continue
                    
                # Filter neighbor possibilities based on current cell's state
                valid_tiles = set()
                for neighbor_tile in neighbor.possibilities:
                    for current_tile in (cell.possibilities if not cell.collapsed else [cell.chosen]):
                        if current_tile and current_tile.can_connect(neighbor_tile, direction):
                            valid_tiles.add(neighbor_tile)
                            break
                
                if len(valid_tiles) < len(neighbor.possibilities):
                    neighbor.possibilities = valid_tiles
                    if not neighbor.possibilities:
                        return False  # Contradiction
                    queue.append(neighbor_pos)
        
        return True
    
    def _find_minimum_entropy_cell(self) -> Optional[Cell]:
        """Find uncollapsed cell with minimum entropy for next collapse."""
        candidates = [c for c in self.grid.values() if not c.collapsed and len(c.possibilities) > 0]
        return min(candidates, key=lambda c: c.entropy) if candidates else None
    
    def _collapse_cell(self, cell: Cell) -> bool:
        """Collapse cell to single state based on weighted random choice."""
        if not cell.possibilities:
            return False
        
        tiles = list(cell.possibilities)
        weights = [t.weight for t in tiles]
        cell.chosen = random.choices(tiles, weights=weights)[0]
        cell.possibilities = {cell.chosen}
        cell.collapsed = True
        return True
    
    def generate(self, verbose: bool = False) -> bool:
        """Execute wave function collapse algorithm.
        
        Returns:
            True if successful, False if contradiction encountered.
        """
        iterations = 0
        while True:
            iterations += 1
            
            # Find next cell to collapse
            cell = self._find_minimum_entropy_cell()
            if not cell:
                break  # All cells collapsed or empty
            
            # Collapse the cell
            if not self._collapse_cell(cell):
                if verbose:
                    print(f"Contradiction at {cell.position}", file=sys.stderr)
                return False
            
            # Propagate constraints
            if not self._propagate(cell.position):
                if verbose:
                    print(f"Propagation failure from {cell.position}", file=sys.stderr)
                return False
            
            if verbose and iterations % 10 == 0:
                print(f"Iteration {iterations}: Collapsed {sum(1 for c in self.grid.values() if c.collapsed)}/{len(self.grid)} cells", file=sys.stderr)
        
        return all(c.collapsed for c in self.grid.values())
    
    def render(self) -> str:
        """Render the generated pattern as ASCII art."""
        lines = []
        for y in range(self.height):
            line = []
            for x in range(self.width):
                cell = self.grid[(x, y)]
                if cell.collapsed and cell.chosen:
                    line.append(cell.chosen.symbol)
                else:
                    line.append('?')
            lines.append(''.join(line))
        return '\n'.join(lines)

# ============================================================================
# CLI INTERFACE
# ============================================================================

def main() -> int:
    """Main entry point with CLI argument parsing."""
    parser = argparse.ArgumentParser(
        description="Generate patterns using Wave Function Collapse algorithm",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="Examples:\n"
               "  python wfc.py --pattern circuit --size 30\n"
               "  python wfc.py --pattern maze --seed 123 --verbose\n"
               "  python wfc.py --test"
    )
    
    parser.add_argument('--seed', type=int, default=DEFAULT_SEED,
                       help=f'Random seed for reproducibility (default: {DEFAULT_SEED})')
    parser.add_argument('--size', type=int, default=DEFAULT_SIZE,
                       help=f'Grid size (default: {DEFAULT_SIZE}x{DEFAULT_SIZE})')
    parser.add_argument('--pattern', type=str, choices=[p.name.lower() for p in Pattern],
                       default='circuit', help='Pattern type to generate')
    parser.add_argument('--verbose', action='store_true',
                       help='Enable verbose output')
    parser.add_argument('--test', action='store_true',
                       help='Run unit tests')
    parser.add_argument('--format', choices=['text', 'json'], default='text',
                       help='Output format (default: text)')
    
    args = parser.parse_args()
    
    if args.test:
        unittest.main(argv=[''], exit=False, verbosity=2)
        return 0
    
    # Generate pattern
    pattern_type = Pattern[args.pattern.upper()]
    tileset = get_tileset(pattern_type)
    generator = WFCGenerator(args.size, args.size, tileset, args.seed)
    
    success = generator.generate(verbose=args.verbose)
    
    if not success:
        print("Failed to generate pattern (contradiction encountered)", file=sys.stderr)
        return 1
    
    if args.format == 'json':
        import json
        output = {
            'pattern': args.pattern,
            'size': args.size,
            'seed': args.seed,
            'grid': generator.render()
        }
        print(json.dumps(output, indent=2))
    else:
        print(generator.render())
    
    return 0

# ============================================================================
# UNIT TESTS
# ============================================================================

class TestWFC(unittest.TestCase):
    """Unit tests for Wave Function Collapse implementation."""
    
    def test_tile_connectivity(self):
        """Test tile connection logic."""
        t1 = Tile('─', frozenset(['E', 'W']))
        t2 = Tile('│', frozenset(['N', 'S']))
        t3 = Tile('┌', frozenset(['S', 'E']))
        
        self.assertTrue(t1.can_connect(t1, 'E'))  # Horizontal to horizontal
        self.assertFalse(t1.can_connect(t2, 'E'))  # Horizontal to vertical
        self.assertTrue(t3.can_connect(t1, 'E'))   # Corner to horizontal
    
    def test_small_generation(self):
        """Test generation on small grid."""
        tileset = get_tileset(Pattern.MAZE)
        gen = WFCGenerator(3, 3, tileset, seed=42)
        success = gen.generate()
        self.assertTrue(success)
        output = gen.render()
        self.assertEqual(len(output.split('\n')), 3)
        self.assertNotIn('?', output)
    
    def test_deterministic_seed(self):
        """Test reproducibility with same seed."""
        tileset = get_tileset(Pattern.CIRCUIT)
        gen1 = WFCGenerator(5, 5, tileset, seed=123)
        gen2 = WFCGenerator(5, 5, tileset, seed=123)
        
        gen1.generate()
        gen2.generate()
        
        self.assertEqual(gen1.render(), gen2.render())

if __name__ == '__main__':
    sys.exit(main())