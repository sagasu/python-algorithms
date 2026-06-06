from typing import List


class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        total = sum(nums)
        ans = []
        left = 0
        for v in nums:
            right = total - left - v
            ans.append(abs(left - right))
            left += v
        return ans
