class Solution(object):
    def maximalSquare(self, matrix):
        dp, ans = [[0] * len(matrix[0]) for row in matrix], 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == '1':
                    dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1
                    ans = max(ans, dp[i][j] ** 2)
        return ans