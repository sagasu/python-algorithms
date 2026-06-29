from typing import List
from collections import deque


class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])

        # For each street type, which directions does it connect?
        # Directions: 0=left, 1=right, 2=up, 3=down
        # connects[street] = set of directions it opens
        connects = {
            1: {0, 1},      # ─  left-right
            2: {2, 3},      # │  up-down
            3: {0, 3},      # ┘  left-down
            4: {1, 3},      # └  right-down
            5: {0, 2},      # ┐  left-up
            6: {1, 2},      # ┌  right-up
        }

        # Direction vectors and their opposites
        dirs = {0: (0, -1), 1: (0, 1), 2: (-1, 0), 3: (1, 0)}
        opposite = {0: 1, 1: 0, 2: 3, 3: 2}

        visited = [[False] * n for _ in range(m)]
        visited[0][0] = True
        q = deque([(0, 0)])

        while q:
            r, c = q.popleft()
            if r == m - 1 and c == n - 1:
                return True
            for d, (dr, dc) in dirs.items():
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and not visited[nr][nc]:
                    # Current cell must open in direction d
                    # Neighbor must open in the opposite direction
                    if d in connects[grid[r][c]] and opposite[d] in connects[grid[nr][nc]]:
                        visited[nr][nc] = True
                        q.append((nr, nc))

        return False
