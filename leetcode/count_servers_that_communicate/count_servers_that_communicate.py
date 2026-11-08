from __future__ import annotations


class Solution:
    def countServers(self, grid: list[list[int]]) -> int:
        """Count servers whose row or column has at least one other server."""
        m, n = len(grid), len(grid[0])
        row_count = [sum(row) for row in grid]
        col_count = [sum(grid[i][j] for i in range(m)) for j in range(n)]
        return sum(
            1
            for i in range(m)
            for j in range(n)
            if grid[i][j] and (row_count[i] > 1 or col_count[j] > 1)
        )


if __name__ == "__main__":
    sol = Solution()
    tests = [
        ([[1, 0], [0, 1]], 0),
        ([[1, 0], [1, 1]], 3),
        ([[1, 1, 0, 0], [0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 0, 1]], 4),
    ]
    failed = False
    for grid, expected in tests:
        got = sol.countServers(grid)
        if got == expected:
            print("OK")
        else:
            print("FAIL")
            failed = True
    if failed:
        raise SystemExit(1)
