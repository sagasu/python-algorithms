class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        N = numRows
        dp = []
        dp.append([1])

        dp[0][0] = 1
        for x in range(1,N):
            dp.append([])
            for y in range(x+1):
                v = 0
                if y < x:
                    v += dp[x-1][y]
                if y >= 1:
                    v += dp[x-1][y-1]
                dp[x].append(v)
        return dp