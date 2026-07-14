from math import gcd
from typing import List

MOD = 10**9 + 7


class Solution:
    def subsequencePairCount(self, nums: List[int]) -> int:
        """
        Count ordered pairs of disjoint non-empty subsequences (seq1, seq2)
        with gcd(seq1) == gcd(seq2). Answer modulo 10^9+7.

        For each nums[i], assign it to: neither, seq1, or seq2.
        DP state (x, y) = number of ways so far with gcd(seq1)=x, gcd(seq2)=y,
        where 0 means the subsequence is still empty.
        """
        m = max(nums)
        # dp[x][y] = ways to reach gcd pair (x, y)
        dp = [[0] * (m + 1) for _ in range(m + 1)]
        dp[0][0] = 1

        for num in nums:
            ndp = [[0] * (m + 1) for _ in range(m + 1)]
            for x in range(m + 1):
                row = dp[x]
                for y in range(m + 1):
                    ways = row[y]
                    if ways == 0:
                        continue
                    # 1) skip num
                    ndp[x][y] = (ndp[x][y] + ways) % MOD
                    # 2) put num in seq1  (gcd(0, num) == num)
                    nx = gcd(x, num)
                    ndp[nx][y] = (ndp[nx][y] + ways) % MOD
                    # 3) put num in seq2
                    ny = gcd(y, num)
                    ndp[x][ny] = (ndp[x][ny] + ways) % MOD
            dp = ndp

        return sum(dp[g][g] for g in range(1, m + 1)) % MOD
