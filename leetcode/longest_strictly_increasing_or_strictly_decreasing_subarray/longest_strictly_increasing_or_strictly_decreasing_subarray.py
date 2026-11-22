from typing import List


class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        """Scan once, tracking the current strictly increasing and decreasing run lengths."""
        ans = inc = dec = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                inc += 1
                dec = 1
            elif nums[i] < nums[i - 1]:
                dec += 1
                inc = 1
            else:
                inc = dec = 1
            ans = max(ans, inc, dec)
        return ans


if __name__ == "__main__":
    sol = Solution()
    tests = [
        ([1, 4, 3, 3, 2], 2),
        ([3, 3, 3, 3], 1),
        ([3, 2, 1], 3),
    ]
    failed = False
    for nums, expected in tests:
        got = sol.longestMonotonicSubarray(nums)
        if got == expected:
            print("OK")
        else:
            print("FAIL")
            failed = True
    if failed:
        raise SystemExit(1)
