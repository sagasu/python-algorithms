class Solution:
    def minimumDistance(self, word: str) -> int:
        def cost(a: int, b: int) -> int:
            # a or b == 26 means finger not yet placed -> free move
            if a == 26 or b == 26:
                return 0
            return abs(a // 6 - b // 6) + abs(a % 6 - b % 6)

        INF = float('inf')
        # dp[j] = min cost so far, where the "other" finger is on letter j (26 = unplaced)
        # The "active" finger just typed word[i-1]
        dp = [INF] * 27
        dp[26] = 0  # start: active finger on word[0] (free), other finger unplaced

        for i in range(1, len(word)):
            cur = ord(word[i]) - ord('A')
            prv = ord(word[i - 1]) - ord('A')
            ndp = [INF] * 27

            for j in range(27):
                if dp[j] == INF:
                    continue
                # Active finger on prv, other finger on j
                # Option 1: active finger moves prv -> cur, other stays at j
                c = dp[j] + cost(prv, cur)
                if c < ndp[j]:
                    ndp[j] = c
                # Option 2: other finger (j) moves to cur, active finger stays at prv
                c = dp[j] + cost(j, cur)
                if c < ndp[prv]:
                    ndp[prv] = c

            dp = ndp

        return min(dp)
