from typing import List


class Solution:
    # Sort, then for each value first extend a run by incrementing, then by keeping it.
    def maxSelectedElements(self, nums: List[int]) -> int:
        nums.sort()
        dp = {}
        for num in nums:
            dp[num + 1] = dp.get(num, 0) + 1
            dp[num] = dp.get(num - 1, 0) + 1
        return max(dp.values())


if __name__ == "__main__":
    sol = Solution()
    tests = [
        ([2, 1, 5, 1, 1], 3),
        ([1, 4, 7, 10], 1),
    ]
    failed = False
    for nums, expected in tests:
        got = sol.maxSelectedElements(nums)
        if got == expected:
            print("OK")
        else:
            print("FAIL")
            failed = True
    if failed:
        raise SystemExit(1)
