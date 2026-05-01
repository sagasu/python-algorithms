from typing import List


class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        n = len(nums)
        total = sum(nums)

        # F(0) = 0*nums[0] + 1*nums[1] + ... + (n-1)*nums[n-1]
        f = sum(i * v for i, v in enumerate(nums))
        ans = f

        # F(k+1) = F(k) + total - n * nums[n-1-k]
        # Each rotation: all indices +1 (adds total), but the last element
        # wraps from index n-1 to 0, losing n * that element's value
        for k in range(1, n):
            f += total - n * nums[n - k]
            ans = max(ans, f)

        return ans
