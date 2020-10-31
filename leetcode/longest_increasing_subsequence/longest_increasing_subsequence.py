from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if(len(nums) == 1):
            return 1
        
        if(len(nums) == 0):
            return 0

        lis = [1 for i in range(len(nums))]
        maxLis = 0
        for i in range(1,len(nums)):
            for j in range(0, i):
                if(nums[j] < nums[i]):
                    if(lis[j] + 1 > lis[i]):
                        lis[i] = lis[j] + 1

            maxLis = max(maxLis, lis[i])



        return maxLis
