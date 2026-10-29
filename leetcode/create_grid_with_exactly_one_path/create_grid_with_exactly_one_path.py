from __future__ import annotations


class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        """Obstacles everywhere except the first row and last column, so the only path is right then down."""
        return ["." * n if i == 0 else "#" * (n - 1) + "." for i in range(m)]


if __name__ == "__main__":
    sol = Solution()

    def exactly_one_path(grid: list[str], m: int, n: int) -> bool:
        if len(grid) != m:
            return False
        if any(len(row) != n or any(ch not in ".#" for ch in row) for row in grid):
            return False
        if grid[0][0] != "." or grid[m - 1][n - 1] != ".":
            return False
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 1
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "#" or (i == 0 and j == 0):
                    continue
                if i:
                    dp[i][j] += dp[i - 1][j]
                if j:
                    dp[i][j] += dp[i][j - 1]
        return dp[m - 1][n - 1] == 1

    tests = [(2, 3), (3, 3), (1, 4)]
    failed = False
    for m, n in tests:
        got = sol.createGrid(m, n)
        if exactly_one_path(got, m, n):
            print("OK")
        else:
            print("FAIL")
            failed = True
    if failed:
        raise SystemExit(1)
