from typing import List


class Solution:
    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0])
        top3 = set()  # keep at most 3 unique largest sums

        def rhombus_sum(i: int, j: int, sz: int) -> int:
            # (i, j) is the TOP vertex. Trace 4 edges:
            # top -> right: go down-right sz steps
            # right -> bottom: go down-left sz steps
            # bottom -> left: go up-left sz steps
            # left -> top: go up-right sz steps
            x, y, total = i, j, 0
            for dx, dy in [(1, 1), (1, -1), (-1, -1), (-1, 1)]:
                for _ in range(sz):
                    x += dx
                    y += dy
                    total += grid[x][y]
            return total

        def add(val: int) -> None:
            top3.add(val)
            if len(top3) > 3:
                top3.discard(min(top3))

        for i in range(m):
            for j in range(n):
                # sz=0 is just the single cell
                add(grid[i][j])
                sz = 1
                # top vertex (i,j), rhombus spans rows [i, i+2*sz] and cols [j-sz, j+sz]
                while i + 2 * sz < m and j - sz >= 0 and j + sz < n:
                    add(rhombus_sum(i, j, sz))
                    sz += 1

        return sorted(top3, reverse=True)
