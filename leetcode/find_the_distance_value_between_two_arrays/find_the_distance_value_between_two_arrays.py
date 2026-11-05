from __future__ import annotations

from bisect import bisect_left


class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        """Sort arr2 and binary-search the closest neighbor of each arr1 value."""
        arr2.sort()
        n = len(arr2)
        ans = 0
        for x in arr1:
            i = bisect_left(arr2, x)
            closest = float("inf")
            if i < n:
                closest = min(closest, abs(arr2[i] - x))
            if i > 0:
                closest = min(closest, abs(arr2[i - 1] - x))
            if closest > d:
                ans += 1
        return ans


if __name__ == "__main__":
    sol = Solution()
    tests = [
        ([4, 5, 8], [10, 9, 1, 8], 2, 2),
        ([1, 4, 2, 3], [-4, -3, 6, 10, 20, 30], 3, 2),
        ([2, 1, 100, 3], [-5, -2, 10, -3, 7], 6, 1),
    ]
    failed = False
    for arr1, arr2, d, expected in tests:
        got = sol.findTheDistanceValue(arr1, arr2, d)
        if got == expected:
            print("OK")
        else:
            print("FAIL")
            failed = True
    if failed:
        raise SystemExit(1)
