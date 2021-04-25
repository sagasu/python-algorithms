class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for layer in range(len(matrix)//2):
            for offset in range(layer, len(matrix) - layer -1):
                t = matrix[len(matrix) - offset -1][layer]
                matrix[len(matrix) - offset -1][layer] = matrix[len(matrix) - layer -1][len(matrix)- offset -1]
                matrix[n - layer -1][n - offset -1] = matrix[offset][n - layer -1]
                matrix[offset][n - layer -1] = matrix[layer][offset]
                matrix[layer][offset] = t
