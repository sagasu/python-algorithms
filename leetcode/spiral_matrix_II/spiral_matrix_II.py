class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        grid = [[0] * n for _ in range(n)]

        x, y = 0, 0
        counter = 1
        directions = [(0,1), (1,0), (0,-1), (-1,0)]
        current_direction = 0

        while counter <= n * n:
            grid[x][y] = counter
            counter += 1

            dx, dy = directions[current_direction]
            nx, ny = x + dx, y + dy

            if not (0 <= nx < n) or not (0 <= ny < n) or grid[nx][ny] > 0:
                current_direction = (current_direction + 1) % 4

                dx, dy = directions[current_direction]
                nx, ny = x + dx, y + dy

            x, y = nx, ny
            
        return grid