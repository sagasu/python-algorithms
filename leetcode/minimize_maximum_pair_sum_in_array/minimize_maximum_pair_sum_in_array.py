class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums)
        return max(sorted_nums[i] + sorted_nums[~i] for i in range(len(nums) // 2))