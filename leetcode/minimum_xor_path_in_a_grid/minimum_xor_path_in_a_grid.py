from __future__ import annotations


class Solution:
    def minCost(self, grid: list[list[int]]) -> int:
        """DP over reachable XOR values at each cell, moving only right or down."""
        m, n = len(grid), len(grid[0])
        dp = [[set() for _ in range(n)] for _ in range(m)]
        dp[0][0].add(grid[0][0])
        for i in range(m):
            for j in range(n):
                val = grid[i][j]
                if i:
                    dp[i][j].update(x ^ val for x in dp[i - 1][j])
                if j:
                    dp[i][j].update(x ^ val for x in dp[i][j - 1])
        return min(dp[m - 1][n - 1])


if __name__ == "__main__":
    sol = Solution()
    tests = [
        ([[1, 2], [3, 4]], 6),
        ([[6, 7], [5, 8]], 9),
        ([[2, 7, 5]], 0),
    ]
    failed = False
    for grid, expected in tests:
        got = sol.minCost(grid)
        if got == expected:
            print("OK")
        else:
            print("FAIL")
            failed = True
    if failed:
        raise SystemExit(1)
