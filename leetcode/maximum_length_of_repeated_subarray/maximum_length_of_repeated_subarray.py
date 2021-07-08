class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:
        dp = [[0] * (len(B)+1) for _ in range(len(A)+1)]
        maxx = 0
        for i in range(len(A)):
            for j in range(len(B)):
                if(A[i] == B[j]):
                    dp[i][j] = dp[i-1][j-1]+1
                    maxx = max(maxx, dp[i][j])
        return maxx