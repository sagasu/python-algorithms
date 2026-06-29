class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        l,r,total,res,n=0,0,0,0,len(nums)
        while r < n:
            total+= nums[r]
            
            while nums[r] * (r - l + 1) > total + k:
                total-=nums[l]
                l+=1
            
            res=max(res, r - l + 1)
            r+=1
        return res