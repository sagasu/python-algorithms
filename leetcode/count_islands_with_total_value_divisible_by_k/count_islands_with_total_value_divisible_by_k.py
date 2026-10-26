from typing import List


class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        """Flood-fill each 4-connected land island and count those whose sum is divisible by k."""
        m, n = len(grid), len(grid[0])
        ans = 0

        def flood(r: int, c: int) -> int:
            stack = [(r, c)]
            total = grid[r][c]
            grid[r][c] = 0
            while stack:
                i, j = stack.pop()
                for ni, nj in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                    if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] > 0:
                        total += grid[ni][nj]
                        grid[ni][nj] = 0
                        stack.append((ni, nj))
            return total

        for i in range(m):
            for j in range(n):
                if grid[i][j] > 0 and flood(i, j) % k == 0:
                    ans += 1
        return ans


if __name__ == "__main__":
    sol = Solution()
    tests = [
        (
            [
                [0, 2, 1, 0, 0],
                [0, 5, 0, 0, 5],
                [0, 0, 1, 0, 0],
                [0, 1, 4, 7, 0],
                [0, 2, 0, 0, 8],
            ],
            5,
            2,
        ),
        (
            [
                [3, 0, 3, 0],
                [0, 3, 0, 3],
                [3, 0, 3, 0],
            ],
            3,
            6,
        ),
    ]
    failed = False
    for grid, k, expected in tests:
        got = sol.countIslands(grid, k)
        if got == expected:
            print("OK")
        else:
            print("FAIL")
            failed = True
    if failed:
        raise SystemExit(1)
