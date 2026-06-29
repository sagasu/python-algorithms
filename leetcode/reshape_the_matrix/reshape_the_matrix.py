class Solution:
    def matrixReshape(self, mat: List[List[int]], newRows: int, newCols: int) -> List[List[int]]:
        rows = len(mat)
        cols = len(mat[0])

        if rows * cols != newRows * newCols:
            return mat

        newMat = [[0] * newCols for _ in range(newRows)]

        for x in range(rows):
            for y in range(cols):
                num = x * cols + y

                newMat[num // newCols][num % newCols] = mat[x][y]
        return newMat