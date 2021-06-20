class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        N = len(grid)
        parents = {}

        def ufind(coords):
            if parents[coords] != coords:
                parents[coords] = ufind(parents[coords])
            return parents[coords]

        def uunion(ca, cb):
            pa = ufind(ca)
            bp = ufind(cb)
            parents[pa] = pb

        events = []
        for x in range(N):
            for y in range(N):
                parents[(x,y)] = (x,y)
                events.append((grid[x][y], x, y))

        directions = [(0,1), (1,0),(-1,0),(0,-1)]
        events.sort()
        for v,x,y in events:
            for dx, dy in directions:
                nx, ny = x + dx, y + dy

                if 0 <= nx < N and 0 <= ny < N and grid[nx][ny] < grid[x][y]:
                    uunion((x,y), (nx,ny))
            if ufind((0,0)) == ufind((N-1, N-1)):
                return v
        return -1