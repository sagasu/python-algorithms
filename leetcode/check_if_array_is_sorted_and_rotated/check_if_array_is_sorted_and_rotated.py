from typing import List


class Solution:
    def check(self, nums: List[int]) -> bool:
        n = len(nums)
        drops = sum(nums[i] > nums[(i + 1) % n] for i in range(n))
        return drops <= 1
