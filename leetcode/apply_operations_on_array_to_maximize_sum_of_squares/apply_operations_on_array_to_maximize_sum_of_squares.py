from typing import List

MOD = 10**9 + 7


class Solution:
    def maxSum(self, nums: List[int], k: int) -> int:
        """
        AND/OR moves bits between numbers without changing each bit's total count.
        Greedily form k numbers: the i-th gets every bit that appears at least i+1
        times. That packing is most unbalanced, so the sum of squares is maximal.
        """
        cnt = [0] * 30
        for x in nums:
            for b in range(30):
                cnt[b] += (x >> b) & 1

        vals = [0] * k
        for b, c in enumerate(cnt):
            bit = 1 << b
            for i in range(min(c, k)):
                vals[i] |= bit

        return sum(v * v for v in vals) % MOD


if __name__ == "__main__":
    sol = Solution()
    tests = [
        ([2, 6, 5, 8], 2, 261),
        ([4, 5, 4, 7], 3, 90),
    ]
    failed = False
    for nums, k, expected in tests:
        got = sol.maxSum(nums, k)
        status = "OK" if got == expected else "FAIL"
        if got != expected:
            failed = True
        print(f"{status}: nums={nums} k={k} -> {got} (expected {expected})")
    if failed:
        raise SystemExit(1)
