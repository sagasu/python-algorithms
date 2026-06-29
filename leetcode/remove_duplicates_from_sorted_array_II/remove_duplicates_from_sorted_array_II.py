class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        pointer = 2
        while pointer < len(nums):
            if nums[pointer] == nums[pointer-2]: nums[:] = nums[:pointer] + nums[pointer+1:]
            else: pointer += 1
        return pointer