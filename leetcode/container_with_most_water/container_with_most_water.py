class Solution:
    def maxArea(self, height: List[int]) -> int:
        N = len(height)

        def getSweepMaxArea(height):
            maxs = []

            best = 0
            for right in range(N):
                index = bisect.bisect_left(maxs, (height[right],0))

                if index >= len(maxs):
                    maxs.append((height[right], right))
                else:
                    area = (right - maxs[index][1]) * height[right]
                    best = max(area, best)

            return best

        return max(getSweepMaxArea(height),  getSweepMaxArea(height[::-1]))