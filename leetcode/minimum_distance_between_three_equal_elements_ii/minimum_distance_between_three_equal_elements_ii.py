from typing import List
from collections import defaultdict


class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        g = defaultdict(list)
        for i, x in enumerate(nums):
            g[x].append(i)

        ans = float('inf')
        for ls in g.values():
            for h in range(len(ls) - 2):
                ans = min(ans, 2 * (ls[h + 2] - ls[h]))

        return -1 if ans == float('inf') else ans
