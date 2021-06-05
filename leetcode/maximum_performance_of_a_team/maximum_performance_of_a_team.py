class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        mod = 10 ** 9 + 7

        best = 0
        total = 0
        h = []

        for eff, sp in sorted(zip(efficiency, speed), reverse=True):
            total += sp
            heapq.heappush(h, sp)
            while len(h) > k:
                removed = heapq.heappop(h)
                total -= removed

            best = max(best, eff * total)

        return best % mod