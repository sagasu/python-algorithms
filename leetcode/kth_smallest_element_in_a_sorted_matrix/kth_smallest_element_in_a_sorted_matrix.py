class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        rows = len(matrix)
        cols = len(matrix[0])

        x, y = 0,0
        h = []
        done = [[False] * cols for _ in range(rows)]
        heapq.heappush(h, (matrix[x][y], x, y))
        while len(h) > 0:
            current, x, y = heapq.heappop(h)
            k -= 1

            if k == 0:
                return current

            for dx, dy in [(1, 0), (0, 1)]:
                nx, ny = x + dx, y + dy

                if 0 <= nx < rows and 0 <= ny < cols and not done[nx][ny]:
                    done[nx][ny] = True
                    heapq.heappush(h, (matrix[nx][ny], nx, ny))