class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        N = len(nums)
        if N <= 1:
            return

        index = N -2
        while index >= 0 and nums[index] >= nums[index+1]:
            index -= 1

        if index == -1:
            nums.reverse()
            return

        index2 = N -1
        while index2 >= index and nums[index] >= nums[index2]:
            index2 -= 1

        nums[index], nums[index2] = nums[index2], nums[index]

        left = index + 1
        right = N -1

        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1