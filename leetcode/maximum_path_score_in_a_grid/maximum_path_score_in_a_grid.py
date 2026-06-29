from typing import List
from functools import cache


class Solution:
    def maxPathScore(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])

        @cache
        def dfs(i: int, j: int, remaining: int) -> int:
            if i < 0 or j < 0 or remaining < 0:
                return float('-inf')
            if i == 0 and j == 0:
                return 0  # start cell has value 0 (guaranteed)
            val = grid[i][j]
            cost = 1 if val > 0 else 0
            best = max(dfs(i - 1, j, remaining - cost), dfs(i, j - 1, remaining - cost))
            return val + best

        ans = dfs(m - 1, n - 1, k)
        dfs.cache_clear()
        return -1 if ans < 0 else ans
