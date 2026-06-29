from sortedcontainers import SortedList

class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        rows = len(matrix)
        cols = len(matrix[0])
        
        prefix = [[0] * (cols + 1) for _ in range(rows + 1)]
        for x in range(rows):
            for y in range(cols):
                prefix[x+1][y+1] += prefix[x + 1][y] + matrix[x][y]
        for x in range(rows):
            for y in range(cols):
                prefix[x + 1][y + 1] += prefix[x][y + 1]

        best = -(10 ** 10)
        for x1 in range(rows):
            for x2 in range(x1, rows):
                s = SortedList()
                s.add(0)

                for y in range(cols):
                    current = prefix[x2+1][y+1] -prefix[x1][y+1]
                    target = current - k
                    index = s.bisect_left(target)
                    if 0 <= index < len(s):
                        best = max(best, current - s[index])
                    s.add(current)
        return best