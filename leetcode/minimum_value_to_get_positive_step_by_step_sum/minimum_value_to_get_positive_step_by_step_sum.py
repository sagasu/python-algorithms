class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        prefix_sum = 0
        negative_most_offset = float('inf')
        
        for i in range(0, len(nums)):
            prefix_sum += nums[i]
            negative_most_offset = min( prefix_sum, negative_most_offset)
        
        threshold = min( negative_most_offset,  0 )
        
        return abs(threshold)+1