class Solution:
    def numDecodings(self, s: str) -> int:
        MOD = 10 ** 9 + 7
        N = len(s)
        dp = [0] * (N + 1)
        dp[0] = 1

        for index in range(N):
            current = s[index]
            if "1" <= current <= "9":
                dp[index + 1] += dp[index]
            elif current == "*":
                dp[index + 1] += 9 * dp[index]
            
            if index - 1 >= 0:
                prev = s[index - 1]
                if prev == "1":
                    if "0" <= current <= "9":
                        dp[index + 1] += dp[index - 1]
                    elif current == "*":
                        dp[index + 1] += 9 * dp[index - 1]
                elif prev == "2":
                    if "0" <= current <= "6":
                        dp[index + 1] += dp[index - 1]
                    elif current == "*":
                        dp[index + 1] += 6 * dp[index - 1]
                elif prev == "*":
                    if "0" <= current <= "9":
                        dp[index + 1] += dp[index - 1]
                    if "0" <= current <= "6":
                        dp[index + 1] += dp[index - 1]
                    if current == "*":
                        dp[index + 1] += 15 * dp[index - 1]
            dp[index + 1] %= MOD
        return dp[N] % MOD