from typing import List


class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        robot.sort()
        factory.sort()

        # Flatten factories: repeat each factory position by its limit
        locs = []
        for pos, limit in factory:
            locs.extend([pos] * limit)

        m, n = len(robot), len(locs)
        INF = float('inf')

        # dp[i][j] = min cost to assign first i robots using any subset of first j slots
        # Recurrence:
        #   dp[i][j] = min(
        #       dp[i][j-1],              # don't use slot j for robot i (skip slot j)
        #       dp[i-1][j-1] + |robot[i-1] - locs[j-1]|  # assign robot i to slot j
        #   )
        # Base: dp[0][j] = 0 for all j (no robots to assign)
        #       dp[i][0] = INF for i > 0 (robots but no slots)

        # Rolling 1D: dp[j] = previous row (i-1 robots), ndp[j] = current row (i robots)
        dp = [0] * (n + 1)  # dp[0][0..n] = 0

        for i in range(1, m + 1):
            ndp = [INF] * (n + 1)
            # ndp[0] = INF (i robots, 0 slots → impossible)
            for j in range(1, n + 1):
                # Skip slot j: robot i was assigned in slots 1..j-1
                ndp[j] = ndp[j - 1]
                # Assign robot i to slot j
                if dp[j - 1] != INF:
                    ndp[j] = min(ndp[j], dp[j - 1] + abs(robot[i - 1] - locs[j - 1]))
            dp = ndp

        return dp[n]
