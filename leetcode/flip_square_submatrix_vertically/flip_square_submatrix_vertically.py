from typing import List


class Solution:
    def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
        # Swap rows symmetrically within the k×k submatrix to reverse row order
        for i in range(k // 2):
            top = x + i
            bot = x + k - 1 - i
            # Only swap the k columns within the submatrix, not the full rows
            grid[top][y:y + k], grid[bot][y:y + k] = grid[bot][y:y + k], grid[top][y:y + k]
        return grid
