from typing import List


class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        nums = sorted(v for row in grid for v in row)

        # All values must be reachable from each other via steps of x
        r = nums[0] % x
        if any(v % x != r for v in nums):
            return -1

        # Optimal target is the median (minimizes sum of |v - target| / x)
        median = nums[len(nums) // 2]
        return sum(abs(v - median) // x for v in nums)
