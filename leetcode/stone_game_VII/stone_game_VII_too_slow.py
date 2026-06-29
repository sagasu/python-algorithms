class Solution:
    def stoneGameVII(self, stones: List[int]) -> int:
        prefix = [0]

        for x in stones:
            prefix.append(prefix[-1] + x)

        N = len(stones)
        inf = float('inf')

        def score(left, right):
            return prefix[right + 1] - prefix[left]

        @lru_cache(None)
        def go(left, right):
            if left == right:
                return 0

            best = -inf
            best = max(best, -go(left + 1, right) + score(left +1,right))
            best = max(best, -go(left, right -1)+score(left, right-1))

            return best

        return go(0, N-1)