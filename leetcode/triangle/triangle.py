class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        N = len(triangle)
        inf = float("inf")

        dp = [[inf] * (N+1) for _ in range(2)]

        dp[0][0] = 0
        for i in range(N):
            prev = dp[i % 2]
            current = dp[(i + 1) % 2]

            for j in range(i + 1):
                current[j + 1] = min(prev[j], prev[j+1]) + triangle[i][j]

            for index in range(N):
                prev[index] = inf
        return min(current)