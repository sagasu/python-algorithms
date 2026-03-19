from typing import List


class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])

        # px[i][j] = count of 'X' in submatrix (0,0)..(i,j)
        # py[i][j] = count of 'Y' in submatrix (0,0)..(i,j)
        px = [[0] * n for _ in range(m)]
        py = [[0] * n for _ in range(m)]
        ans = 0

        for i in range(m):
            for j in range(n):
                up_x  = px[i - 1][j] if i > 0 else 0
                up_y  = py[i - 1][j] if i > 0 else 0
                lft_x = px[i][j - 1] if j > 0 else 0
                lft_y = py[i][j - 1] if j > 0 else 0
                diag_x = px[i - 1][j - 1] if i > 0 and j > 0 else 0
                diag_y = py[i - 1][j - 1] if i > 0 and j > 0 else 0

                px[i][j] = (grid[i][j] == 'X') + up_x + lft_x - diag_x
                py[i][j] = (grid[i][j] == 'Y') + up_y + lft_y - diag_y

                if px[i][j] > 0 and px[i][j] == py[i][j]:
                    ans += 1

        return ans
