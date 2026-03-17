from typing import List


class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])

        # height[j] = number of consecutive 1s ending at current row in column j
        height = [0] * n

        ans = 0
        for i in range(m):
            # Update heights
            for j in range(n):
                height[j] = height[j] + 1 if matrix[i][j] == 1 else 0

            # Sort descending — since we can rearrange columns freely,
            # the k tallest columns can form a rectangle of height = min of those k heights
            # = the k-th largest height (0-indexed: sorted_desc[k-1])
            for k, h in enumerate(sorted(height, reverse=True), start=1):
                if h == 0:
                    break  # remaining heights are all 0, no point continuing
                ans = max(ans, k * h)

        return ans
