class Solution:
    def stoneGameVII(self, stones: List[int]) -> int:
        N = len(stones)

        is_cached = [[False] * (N) for _ in range(N)]
        cache = [[0] * (N) for _ in range(N)]


        prefix = [0]
        for x in stones:
            prefix.append(prefix[-1] + x)

        def maxDiff(left, right):
            if left == right:
                return 0
            if is_cached[left][right]:
                return cache[left][right]

            leftScore = (prefix[right + 1] - prefix[left + 1]) - maxDiff(left +1,right)
            rightScore = (prefix[right] - prefix[left]) - maxDiff(left, right -1)

            is_cached[left][right] = True
            cache[left][right] = max(leftScore, rightScore)
            return cache[left][right]

        return maxDiff(0, N-1)