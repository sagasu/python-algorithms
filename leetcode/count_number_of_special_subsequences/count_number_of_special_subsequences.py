class Solution:
    def countSpecialSubsequences(self, nums: List[int]) -> int:
        zero=0
        one=0
        two=0
        mod=10**9+7
        
        for i in range(len(nums)):
            
            if nums[i]==0:
                zero = (2*zero+1)%mod
            elif nums[i]==1:
                one=(2*one+zero)%mod
            elif nums[i]==2:
                two = (2*two+one)%mod
        return two%mod