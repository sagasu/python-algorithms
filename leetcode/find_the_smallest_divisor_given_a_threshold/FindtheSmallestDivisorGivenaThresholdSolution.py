from typing import List

class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        
        def good(mid):
            maxSum = 0
            for num in nums:
                maxSum += (mid + num -1) // mid

            return maxSum <= threshold
        
        left = 1
        right = (10 ** 6) + 1

        while left < right:
            mid = (left + right) // 2

            if good(mid):
                right = mid
            else:
                left = mid + 1

        return left
