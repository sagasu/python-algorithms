class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        done = [[False] * cols for _ in range(rows)]
        direction = [(0,1), (1,0), (-1,0), (0,-1)]

        def area(x,y):
            if done[x][y]:
                return 0

            done[x][y] = True
            total = 1

            for dx, dy in direction:
                nx, ny = x + dx, y + dy

                if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 1:
                    total += area(nx, ny)

            return total

        mx = 0
        for x in range(rows):
            for y in range(cols):
                if grid[x][y] == 1 and not done[x][y]:
                    mx = max(mx, area(x,y))
        return mx