from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] > nums[hi]:
                lo = mid + 1   # min is in right half
            elif nums[mid] < nums[hi]:
                hi = mid       # min is in left half (including mid)
            else:
                hi -= 1        # can't tell — safely shrink hi
        return nums[lo]
