from typing import List


class Solution:
    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])

        def get_ring(layer: int) -> List[tuple]:
            """Return (row, col) positions of the ring in clockwise order."""
            cells = []
            r1, c1 = layer, layer
            r2, c2 = m - 1 - layer, n - 1 - layer
            # Top row: left to right
            for c in range(c1, c2 + 1):
                cells.append((r1, c))
            # Right col: top+1 to bottom
            for r in range(r1 + 1, r2 + 1):
                cells.append((r, c2))
            # Bottom row: right-1 to left
            for c in range(c2 - 1, c1 - 1, -1):
                cells.append((r2, c))
            # Left col: bottom-1 to top+1
            for r in range(r2 - 1, r1, -1):
                cells.append((r, c1))
            return cells

        layers = min(m, n) // 2
        for layer in range(layers):
            cells = get_ring(layer)
            size = len(cells)
            shift = k % size
            # Extract values, rotate left by shift
            vals = [grid[r][c] for r, c in cells]
            vals = vals[shift:] + vals[:shift]
            # Write back
            for (r, c), v in zip(cells, vals):
                grid[r][c] = v

        return grid
