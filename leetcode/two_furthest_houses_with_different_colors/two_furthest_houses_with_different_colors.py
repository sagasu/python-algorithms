from typing import List


class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        n = len(colors)
        ans = 0
        # Scan from left: for each i, find the rightmost j != colors[i]
        # Equivalently: check pairs (0, j) from right, and (i, n-1) from left
        # But that misses middle pairs. Use two passes instead:
        # Pass 1: fix i=0, scan j from right
        # Pass 2: fix j=n-1, scan i from left
        # These two passes cover all optimal pairs because the max-distance pair
        # must have one end being either the leftmost or rightmost occurrence
        # of its color — but that's not guaranteed either.
        # Simplest correct O(n^2): check all pairs
        for i in range(n):
            for j in range(i + 1, n):
                if colors[i] != colors[j]:
                    ans = max(ans, j - i)
        return ans
