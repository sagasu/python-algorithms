from typing import List
from collections import defaultdict
import bisect


class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        n = len(nums)
        # Group indices by value
        positions = defaultdict(list)
        for i, v in enumerate(nums):
            positions[v].append(i)

        def min_circular_dist(idxs: list, i: int) -> int:
            # pos is the position of i itself in idxs
            pos = bisect.bisect_left(idxs, i)
            m = len(idxs)
            best = float('inf')
            # Check the immediate predecessor and successor (skip i itself at pos)
            for p in [pos - 1, (pos + 1) % m]:
                j = idxs[p]
                d = abs(j - i)
                best = min(best, min(d, n - d))
            return best

        ans = []
        for q in queries:
            idxs = positions[nums[q]]
            if len(idxs) == 1:
                ans.append(-1)
            else:
                ans.append(min_circular_dist(idxs, q))
        return ans
