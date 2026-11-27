from math import gcd
from typing import List


class Solution:
    # Any pair works. A longer subarray works while its product equals lcm * gcd.
    def maxLength(self, nums: List[int]) -> int:
        n = len(nums)
        best = 0
        for i in range(n):
            g = 0
            lcm = 1
            prod = 1
            for j in range(i, n):
                x = nums[j]
                g = gcd(g, x)
                lcm = lcm // gcd(lcm, x) * x
                prod *= x
                if prod == lcm * g:
                    best = max(best, j - i + 1)
        return best


if __name__ == "__main__":
    sol = Solution()
    tests = [
        ([1, 2, 1, 2, 1, 1, 1], 5),
        ([2, 3, 4, 5, 6], 3),
        ([1, 2, 3, 1, 4, 5, 1], 5),
    ]
    failed = False
    for nums, expected in tests:
        got = sol.maxLength(nums)
        if got == expected:
            print("OK")
        else:
            print("FAIL")
            failed = True
    if failed:
        raise SystemExit(1)
