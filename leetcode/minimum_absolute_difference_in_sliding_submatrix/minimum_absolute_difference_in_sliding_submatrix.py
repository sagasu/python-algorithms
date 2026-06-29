from typing import List
from itertools import pairwise


class Solution:
    def minAbsDiff(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        ans = [[0] * (n - k + 1) for _ in range(m - k + 1)]

        for i in range(m - k + 1):
            for j in range(n - k + 1):
                # Collect all k*k values, sort, then min diff is between adjacent distinct elements
                nums = sorted(grid[x][y] for x in range(i, i + k) for y in range(j, j + k))
                ans[i][j] = min((b - a for a, b in pairwise(nums) if a != b), default=0)

        return ans
