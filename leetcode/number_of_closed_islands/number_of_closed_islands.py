from typing import List


class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        """Flood-fill land touching the border, then count remaining 0-islands."""
        m, n = len(grid), len(grid[0])

        def flood(r: int, c: int) -> None:
            stack = [(r, c)]
            grid[r][c] = 1
            while stack:
                i, j = stack.pop()
                for ni, nj in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                    if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] == 0:
                        grid[ni][nj] = 1
                        stack.append((ni, nj))

        for i in range(m):
            if grid[i][0] == 0:
                flood(i, 0)
            if grid[i][n - 1] == 0:
                flood(i, n - 1)
        for j in range(n):
            if grid[0][j] == 0:
                flood(0, j)
            if grid[m - 1][j] == 0:
                flood(m - 1, j)

        closed = 0
        for i in range(1, m - 1):
            for j in range(1, n - 1):
                if grid[i][j] == 0:
                    flood(i, j)
                    closed += 1
        return closed


if __name__ == "__main__":
    sol = Solution()
    tests = [
        (
            [
                [1, 1, 1, 1, 1, 1, 1, 0],
                [1, 0, 0, 0, 0, 1, 1, 0],
                [1, 0, 1, 0, 1, 1, 1, 0],
                [1, 0, 0, 0, 0, 1, 0, 1],
                [1, 1, 1, 1, 1, 1, 1, 0],
            ],
            2,
        ),
        (
            [
                [0, 0, 1, 0, 0],
                [0, 1, 0, 1, 0],
                [0, 1, 1, 1, 0],
            ],
            1,
        ),
        (
            [
                [1, 1, 1, 1, 1, 1, 1],
                [1, 0, 0, 0, 0, 0, 1],
                [1, 0, 1, 1, 1, 0, 1],
                [1, 0, 1, 0, 1, 0, 1],
                [1, 0, 1, 1, 1, 0, 1],
                [1, 0, 0, 0, 0, 0, 1],
                [1, 1, 1, 1, 1, 1, 1],
            ],
            2,
        ),
    ]
    failed = False
    for grid, expected in tests:
        got = sol.closedIsland(grid)
        if got == expected:
            print("OK")
        else:
            print("FAIL")
            failed = True
    if failed:
        raise SystemExit(1)
