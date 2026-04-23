from typing import List
from collections import defaultdict


class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * n

        # Group indices by value
        groups = defaultdict(list)
        for i, v in enumerate(nums):
            groups[v].append(i)

        for indices in groups.values():
            k = len(indices)
            # prefix[i] = sum of indices[0..i-1]
            prefix = 0
            for rank, idx in enumerate(indices):
                # Distance to all elements to the left: idx * rank - prefix
                ans[idx] += idx * rank - prefix
                prefix += idx

            suffix = 0
            for rank, idx in enumerate(reversed(indices)):
                # Distance to all elements to the right: suffix - idx * rank
                ans[idx] += suffix - idx * rank
                suffix += idx

        return ans
