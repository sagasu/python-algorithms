class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows = len(heights)
        cols = len(heights[0])

        directions = [(1,0), (-1, 0), (0, 1), (0, -1)]

        def good(effort):
            q = collections.deque()

            seen = set()
            q.append((0, 0))

            while len(q) > 0:
                x, y = q.popleft()

                if x == rows - 1 and y == cols -1:
                    return True
                
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy

                    if 0 <= nx < rows and 0 <= ny < cols and abs(heights[x][y] - heights[nx][ny]) <= effort and (nx, ny) not in seen:
                        if nx == rows -1 and ny == cols -1:
                            return True

                        seen.add((nx, ny))
                        q.append((nx, ny))

            return False

        left = 0
        right = 1000000

        while left < right:
            mid = (left + right) // 2

            if good(mid):
                right = mid
            else:
                left = mid +1
                
        return left