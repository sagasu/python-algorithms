class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        MOD = 10 ** 9 + 7

        dp = [[0] * (k+1) for _ in range(n+1)]
        dp[0][0] = 1
        prefix = [[0] * (k+1) for _ in range(n+1)]
        prefix[0][0] =1
        for currentk in range(1, k+1):
            prefix[0][currentk] += prefix[0][currentk-1]

        for left in range(1, n+1):
            for currentk in range(0, k+1):
                d = n - left
                dp[left][currentk] = prefix[left-1][currentk]
                if currentk - d - 1 >= 0:
                    dp[left][currentk] -= prefix[left-1][currentk - d -1]

            prefix[left][0] = dp[left][0]
            for currentk in range(1, k+1):
                prefix[left][currentk] += prefix[left][currentk - 1] + dp[left][currentk]
        return dp[n][k] % MOD
