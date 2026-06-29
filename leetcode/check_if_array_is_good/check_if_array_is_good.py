from typing import List
from collections import Counter


class Solution:
    def isGood(self, nums: List[int]) -> bool:
        n = len(nums)
        # Good array = permutation of [1, 2, ..., n-1, n-1]
        # So max must be n-1, appear exactly twice, all others 1..n-2 appear once
        expected = Counter(range(1, n))   # 1 through n-1, each once
        expected[n - 1] += 1             # n-1 appears twice total
        return Counter(nums) == expected
