class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        N = len(cost)
        inf = 10 * 10

        is_cached = [False] * (N + 1)
        cached = [inf] * (N + 1)

        def minCost(step):
            if step >= N + 1:
                return inf
            if is_cached[step]:
                return cached[step]
            if step == N:
                return 0

            c = cost[step] + min(
                minCost(step + 1),
                minCost(step + 2)
            )

            is_cached[step] = True
            cached[step] = c
            return c
            
        return min(minCost(0), minCost(1))