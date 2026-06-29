from typing import List


class Solution:
    def maximumAmount(self, coins: List[List[int]]) -> int:
        m, n = len(coins), len(coins[0])
        NEG_INF = float('-inf')

        # dp[i][j][k] = max coins reaching (i,j) having used k neutralizations (k=0,1,2)
        dp = [[[NEG_INF] * 3 for _ in range(n)] for _ in range(m)]

        for i in range(m):
            for j in range(n):
                val = coins[i][j]
                for k in range(3):
                    # Best value arriving at (i,j) with k neutralizations used
                    prev = NEG_INF
                    if i == 0 and j == 0:
                        prev = 0  # starting point
                    else:
                        if i > 0 and dp[i-1][j][k] != NEG_INF:
                            prev = max(prev, dp[i-1][j][k])
                        if j > 0 and dp[i][j-1][k] != NEG_INF:
                            prev = max(prev, dp[i][j-1][k])

                    if prev == NEG_INF:
                        continue

                    # Option 1: collect val normally
                    dp[i][j][k] = max(dp[i][j][k], prev + val)

                    # Option 2: neutralize val (skip it), costs one neutralization
                    if k > 0:
                        prev_k1 = NEG_INF
                        if i == 0 and j == 0:
                            prev_k1 = 0
                        else:
                            if i > 0 and dp[i-1][j][k-1] != NEG_INF:
                                prev_k1 = max(prev_k1, dp[i-1][j][k-1])
                            if j > 0 and dp[i][j-1][k-1] != NEG_INF:
                                prev_k1 = max(prev_k1, dp[i][j-1][k-1])
                        if prev_k1 != NEG_INF:
                            dp[i][j][k] = max(dp[i][j][k], prev_k1)  # skip val, keep prev sum

        return max(dp[m-1][n-1])
