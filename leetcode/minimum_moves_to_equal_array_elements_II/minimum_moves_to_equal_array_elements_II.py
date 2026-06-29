class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        mn = min(nums)
        nums = [x - mn for x in nums]
        nums.sort()
        N = len(nums)

        left = 0
        previous = 0
        right = sum(nums)
        best = 10 ** 10

        for index in range(N):
            delta = nums[index] - previous

            left_count = index
            left += left_count * delta
            right_count = N - index -1
            right -= (right_count + 1) * delta

            total = left + right
            best = min(best, total)
            previous = nums[index]
        return best