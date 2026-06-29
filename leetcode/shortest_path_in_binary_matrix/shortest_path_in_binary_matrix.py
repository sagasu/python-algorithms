class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        N = len(grid)
        queue = collections.deque()
        seen =  [[False] * N for _ in range(N)]

        def maybeEnque(d, x, y):
            if not (0 <= x < N and 0 <= y < N):
                return
            if seen[x][y]:
                return
            if grid[x][y] != 0:
                return

            enqued(d, x, y)

        def enqued(d, x, y):
            seen[x][y] = True
            queue.append((d,x,y))

        maybeEnque(1,0,0)

        while len(queue) > 0:
            d, x, y =queue.popleft()

            if x == N -1 and y == N-1:
                return d

            for dx in range(-1, 1 +1):
                for dy in range(-1, 1+1):
                    nx, ny = x +dx, y + dy

                    maybeEnque(d +1, nx, ny)

        return -1