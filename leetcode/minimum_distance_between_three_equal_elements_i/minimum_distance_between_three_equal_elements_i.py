from typing import List
from collections import defaultdict


class Solution:
    def minDistance(self, nums: List[int]) -> int:
        # For sorted indices i < j < k: |i-j|+|j-k|+|k-i| = 2*(k-i)
        # So minimize 2*(third - first) over all consecutive triples of same value.
        positions = defaultdict(list)
        for i, v in enumerate(nums):
            positions[v].append(i)

        ans = float('inf')
        for idxs in positions.values():
            if len(idxs) >= 3:
                for t in range(len(idxs) - 2):
                    ans = min(ans, 2 * (idxs[t + 2] - idxs[t]))

        return ans if ans != float('inf') else -1
