from typing import Collection


class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        mx = 0
        N = len(nums)
        f = collections.Counter()
        total = 0

        left = right = 0
        while right < N:
            f[nums[right]] += 1
            total += nums[right]

            while f[nums[right]] > 1:
                f[nums[left]] -= 1
                total -= nums[left]
                left += 1

            mx = max(mx, total)
            right +=1
        return mx