from typing import List


class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        """Prefix sums: check every window of length l..r and take the min positive sum."""
        n = len(nums)
        prefix = [0] * (n + 1)
        for i, x in enumerate(nums):
            prefix[i + 1] = prefix[i] + x

        ans = float("inf")
        for i in range(n):
            for length in range(l, r + 1):
                j = i + length
                if j > n:
                    break
                s = prefix[j] - prefix[i]
                if 0 < s < ans:
                    ans = s
        return ans if ans != float("inf") else -1


if __name__ == "__main__":
    sol = Solution()
    tests = [
        ([3, -2, 1, 4], 2, 3, 1),
        ([-2, 2, -3, 1], 2, 3, -1),
        ([1, 2, 3, 4], 2, 4, 3),
    ]
    failed = False
    for nums, l, r, expected in tests:
        got = sol.minimumSumSubarray(nums, l, r)
        if got == expected:
            print("OK")
        else:
            print("FAIL")
            failed = True
    if failed:
        raise SystemExit(1)
