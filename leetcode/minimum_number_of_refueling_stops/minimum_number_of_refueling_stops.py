class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        stations.append([target,0])
        N = len(stations)

        inf = 10 ** 10
        dp = [[-inf] * (N +1) for _ in range(N)]

        if startFuel >= stations[0][0]:
            dp[0][0] = startFuel - stations[0][0]
            dp[0][1] = startFuel - stations[0][0] + stations[0][1]

        for i in range(1,N):
            fuelNeeded = stations[i][0] - stations[i-1][0]
            if startFuel >= stations[i][0]:
                dp[i][0] = startFuel - stations[i][0]
                dp[i][1] = startFuel - stations[i][0] + stations[i][1]

            for j in range(1,N):
                fuelAdded = stations[i][1]
                if dp[i-1][j] >= fuelNeeded and dp[i-1][j] - fuelNeeded > dp[i][j]:
                    dp[i][j] = dp[i-1][j] - fuelNeeded
                if dp[i-1][j-1] >= fuelNeeded and dp[i-1][j-1] - fuelNeeded + fuelAdded > dp[i][j]:
                    dp[i][j] = dp[i-1][j-1] - fuelNeeded + fuelAdded

        for i in range(N):
            if dp[N-1][i] >= 0:
                return i
        return -1