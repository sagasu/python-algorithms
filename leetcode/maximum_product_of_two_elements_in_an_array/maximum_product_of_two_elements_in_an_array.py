from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # (a-1)*(b-1) is maximized by the two largest values (nums[i] >= 1).
        max1 = max2 = 0
        for num in nums:
            if num > max1:
                max2, max1 = max1, num
            elif num > max2:
                max2 = num
        return (max1 - 1) * (max2 - 1)
