from typing import List


class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        """DP: min cost to each step from the previous 1–3 steps."""
        dp = [0] * (n + 1)
        for j in range(1, n + 1):
            best = float("inf")
            for i in range(max(0, j - 3), j):
                best = min(best, dp[i] + costs[j - 1] + (j - i) * (j - i))
            dp[j] = best
        return dp[n]


if __name__ == "__main__":
    sol = Solution()
    tests = [
        (4, [1, 2, 3, 4], 13),
        (4, [5, 1, 6, 2], 11),
        (3, [9, 8, 3], 12),
    ]
    failed = False
    for n, costs, expected in tests:
        got = sol.climbStairs(n, costs)
        if got == expected:
            print("OK")
        else:
            print("FAIL")
            failed = True
    if failed:
        raise SystemExit(1)
