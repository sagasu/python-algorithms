from typing import List


class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        # The best single subarray uses the entire array (global max and min).
        # Pick it k times.
        return (max(nums) - min(nums)) * k
