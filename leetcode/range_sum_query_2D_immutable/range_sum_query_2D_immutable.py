class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        rows = len(matrix)
        cols = len(matrix[0])

        self.prefix = [[0] * (cols+1) for _ in range(rows + 1)]
        for x in range(1, rows + 1):
            for y in range(1, cols +1):
                self.prefix[x][y] = matrix[x-1][y-1]
                self.prefix[x][y] += self.prefix[x][y-1]
        for x in range(1, rows +1):
            for y in range(1, cols + 1):
                self.prefix[x][y] += self.prefix[x-1][y]



    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.prefix[row2+ 1][col2+1] -self.prefix[row1][col2+1]-self.prefix[row2 + 1][col1] + self.prefix[row1][col1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)