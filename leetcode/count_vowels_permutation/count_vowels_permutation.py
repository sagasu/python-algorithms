class Solution:
    def countVowelPermutation(self, n: int) -> int:
        MOD = 10 ** 9 + 7 

        if n == 1: return 5
        
        pdp = [0] * 5
        dp = [0] * 5

        for j in range(5):
            pdp[j] = 1

        for i in range(2, n + 1):
            dp = [0] * 5
            dp[0] = (pdp[1] + pdp[2] + pdp[4]) % MOD
            dp[1] = (pdp[0] + pdp[2]) % MOD
            dp[2] = (pdp[1] + pdp[3]) % MOD
            dp[3] = pdp[2] % MOD
            dp[4] = (pdp[2] + pdp[3]) % MOD

            pdp = dp

        return sum(dp) % MOD