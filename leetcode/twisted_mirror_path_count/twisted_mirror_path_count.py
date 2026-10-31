from typing import List


class Solution:
    def uniquePaths(self, grid: List[List[int]]) -> int:
        """DP on empty cells; a right/down step into a mirror bounces until an empty cell."""
        MOD = 10**9 + 7
        m, n = len(grid), len(grid[0])
        # memo[r][c][d] = landing cell when trying to enter (r, c) facing d (0=right, 1=down)
        memo = [[[None, None] for _ in range(n)] for _ in range(m)]

        def resolve(r: int, c: int, d: int):
            path = []
            result = (-1, -1)
            while 0 <= r < m and 0 <= c < n:
                cached = memo[r][c][d]
                if cached is not None:
                    result = cached
                    break
                path.append((r, c, d))
                if grid[r][c] == 0:
                    result = (r, c)
                    break
                if d == 0:
                    r += 1
                    d = 1
                else:
                    c += 1
                    d = 0
            for pr, pc, pd in path:
                memo[pr][pc][pd] = result
            return None if result[0] < 0 else result

        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 1
        for i in range(m):
            for j in range(n):
                if dp[i][j] == 0:
                    continue
                ways = dp[i][j]
                dest = resolve(i, j + 1, 0)
                if dest is not None:
                    dp[dest[0]][dest[1]] = (dp[dest[0]][dest[1]] + ways) % MOD
                dest = resolve(i + 1, j, 1)
                if dest is not None:
                    dp[dest[0]][dest[1]] = (dp[dest[0]][dest[1]] + ways) % MOD
        return dp[m - 1][n - 1]


if __name__ == "__main__":
    sol = Solution()
    tests = [
        ([[0, 1, 0], [0, 0, 1], [1, 0, 0]], 5),
        ([[0, 0], [0, 0]], 2),
        ([[0, 1, 1], [1, 1, 0]], 1),
    ]
    failed = False
    for grid, expected in tests:
        got = sol.uniquePaths(grid)
        if got == expected:
            print("OK")
        else:
            print("FAIL")
            failed = True
    if failed:
        raise SystemExit(1)
