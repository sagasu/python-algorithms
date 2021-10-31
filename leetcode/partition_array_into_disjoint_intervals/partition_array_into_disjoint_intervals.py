class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        N = len(nums)
        mins = [inf] * N
        
        mins[N-1] = nums[N-1]
        for index in range(N-2, -1, -1):
            mins[index] = min(nums[index], mins[index + 1])
        
        currentMax = 0
        for index in range(0, N-1):
            currentMax = max(currentMax, nums[index])
            
            if currentMax <= mins[index+1]:
                return index+1
        return N
        
