from __future__ import annotations


class Solution:
    def numOfSubarrays(self, arr: list[int]) -> int:
        """Prefix parity: odd-sum subarray ends at prefixes of opposite parity."""
        mod = 10**9 + 7
        even = 1
        odd = 0
        prefix = 0
        ans = 0
        for x in arr:
            prefix ^= x & 1
            if prefix:
                ans += even
                odd += 1
            else:
                ans += odd
                even += 1
        return ans % mod


if __name__ == "__main__":
    sol = Solution()
    tests = [
        ([1, 3, 5], 4),
        ([2, 4, 6], 0),
        ([1, 2, 3, 4, 5, 6, 7], 16),
    ]
    failed = False
    for arr, expected in tests:
        got = sol.numOfSubarrays(arr)
        if got == expected:
            print("OK")
        else:
            print("FAIL")
            failed = True
    if failed:
        raise SystemExit(1)
