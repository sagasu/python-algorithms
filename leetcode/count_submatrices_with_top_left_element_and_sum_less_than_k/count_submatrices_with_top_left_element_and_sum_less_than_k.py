from typing import List


class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])

        # Build 2D prefix sum in-place (or use a copy)
        # prefix[i][j] = sum of submatrix from (0,0) to (i,j)
        prefix = [[0] * n for _ in range(m)]
        ans = 0

        for i in range(m):
            for j in range(n):
                prefix[i][j] = (
                    grid[i][j]
                    + (prefix[i - 1][j] if i > 0 else 0)
                    + (prefix[i][j - 1] if j > 0 else 0)
                    - (prefix[i - 1][j - 1] if i > 0 and j > 0 else 0)
                )
                if prefix[i][j] <= k:
                    ans += 1

        return ans
