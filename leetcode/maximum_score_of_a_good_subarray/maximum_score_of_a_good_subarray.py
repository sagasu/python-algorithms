class Solution:
	def maximumScore(self, nums: List[int], k: int) -> int:

		res, minimum, left, right, sz = nums[k], nums[k], k, k, len(nums)
		
        while left > 0 or right < sz - 1:
            if (nums[left - 1] if left else 0) < (nums[right + 1] if right < sz - 1 else 0):
                right += 1
            else:
                left -= 1
            minimum = min(minimum, nums[left], nums[right])
            res = max(res, minimum * (right - left + 1))
        return res