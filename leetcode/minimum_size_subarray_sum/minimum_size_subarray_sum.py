from sys import maxsize
from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        ans = maxsize
        left = 0
        sum = 0
        for  i in range(n):
            sum += nums[i]
            while (sum >= target):
                ans = min(ans, i + 1 - left)
                sum -= nums[left]
                left += 1
            
        
        return ans if ans != maxsize else 0
    
print(Solution().minSubArrayLen(7, [2,3,1,2,4,3]) == 2)