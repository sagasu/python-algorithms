class Solution:
    def findPaths(self, rows: int, cols: int, maxMove: int, startRow: int, startColumn: int) -> int:
        MOD = 10 ** 9 + 7
        counts = [[([0] * cols) for _ in range(rows)] for _ in range(2)]
        outsideCount = 0

        counts[0][startRow][startColumn] = 1
        directions = [(1,0),(-1,0),(0,1),(0,-1)]

        for move in range(maxMove):
            currentMove = move % 2
            nextMove = (move + 1) % 2

            for x in range(rows):
                for y in range(cols):
                    currentMoves = counts[currentMove][x][y]

                    if currentMoves > 0:
                        for dx, dy in directions:
                            nx, ny = x + dx, y + dy

                            if 0 <= nx < rows and 0 <= ny < cols:
                                counts[nextMove][nx][ny] += currentMoves
                                counts[nextMove][nx][ny] %= MOD
                            else:
                                outsideCount += currentMoves
                                outsideCount %= MOD

            for x in range(rows):
                for y in range(cols):
                    counts[currentMove][x][y] = 0

        return outsideCount % MOD