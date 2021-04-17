class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        rows = len(matrix)
        cols = len(matrix[0])
        prefix = [[0] * (cols + 1) for _ in range(rows + 1)]

        for r in range(rows):
            for c in range(cols):
                prefix[r + 1][c+ 1] = matrix[r][c]
        
        for r in range(rows + 1):
            for c in range(cols):
                prefix[r][c+ 1] += prefix[r][c]

        for r in range(rows):
            for c in range(cols + 1):
                prefix[r + 1][c] += prefix[r][c]

        total = 0
        for r1 in range(1, rows + 1):
            for r2 in range(r1):
                lookup = collections.defaultdict(int)
                lookup[0] = 1

                current = 0
                for c in range(1, cols + 1):
                    current += prefix[r1][c] - prefix[r2][c] - prefix[r1][c - 1] + prefix[r2][c-1]

                    total += lookup[current - target]
                    lookup[current] += 1
        return total

