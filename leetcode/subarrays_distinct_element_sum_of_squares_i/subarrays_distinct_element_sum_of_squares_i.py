from typing import List


class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        """For each start, expand right while tracking distinct values; add distinct^2."""
        n = len(nums)
        ans = 0
        for i in range(n):
            seen = set()
            for j in range(i, n):
                seen.add(nums[j])
                d = len(seen)
                ans += d * d
        return ans


if __name__ == "__main__":
    s = Solution()
    tests = [
        ([1, 2, 1], 15),
        ([1, 1], 3),
    ]
    failed = False
    for nums, expected in tests:
        got = s.sumCounts(nums)
        if got == expected:
            print("OK")
        else:
            print("FAIL")
            failed = True
    if failed:
        raise SystemExit(1)
