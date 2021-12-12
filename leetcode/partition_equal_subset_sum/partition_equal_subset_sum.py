class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        
        if total & 1:
            return False
        
        nums.sort(reverse=True)
        
        @functools.lru_cache(None)
        def dfs(i, total):
            if total < 0:
                return False
            
            if total == 0:
                return True
            
            if i >= len(nums):
                return False
            
            return dfs(i+1, total - nums[i]) or dfs(i+1, total)
        
        return dfs(0,total//2)
