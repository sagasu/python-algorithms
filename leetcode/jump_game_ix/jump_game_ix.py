from typing import List


class Solution:
    def maxValue(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * n

        # pre_max[i] = max(nums[0..i])
        pre_max = [nums[0]] * n
        for i in range(1, n):
            pre_max[i] = max(pre_max[i - 1], nums[i])

        # Traverse right to left, tracking suffix minimum
        suf_min = float('inf')
        for i in range(n - 1, -1, -1):
            # If pre_max[i] > suf_min: there's a smaller value to the right,
            # so we can jump right to it, then continue from i+1's reachable set
            if i == n - 1 or pre_max[i] <= suf_min:
                ans[i] = pre_max[i]
            else:
                ans[i] = ans[i + 1]
            suf_min = min(suf_min, nums[i])

        return ans
