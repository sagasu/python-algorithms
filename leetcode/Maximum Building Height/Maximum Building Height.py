from typing import List

class Solution:
    def maxBuilding(self, n: int, restrictions: List[List[int]]) -> int:
        if not restrictions:
            return n - 1
        
        r = restrictions[:]
        r.append([1, 0])
        r.sort()
        
        # Add the last building if not present
        if r[-1][0] != n:
            r.append([n, n - 1])
        
        m = len(r)
        
        # Forward pass: propagate max possible from left
        for i in range(1, m):
            r[i][1] = min(r[i][1], r[i - 1][1] + r[i][0] - r[i - 1][0])
        
        # Backward pass: propagate max possible from right
        for i in range(m - 2, -1, -1):
            r[i][1] = min(r[i][1], r[i + 1][1] + r[i + 1][0] - r[i][0])
        
        # Find the maximum peak between consecutive restrictions
        ans = 0
        for i in range(m - 1):
            # The max height between two points is the peak of the tent
            # height = min(left + dist, right + (total_dist - dist))
            # max is (h_left + h_right + dist) // 2
            dist = r[i + 1][0] - r[i][0]
            peak = (r[i][1] + r[i + 1][1] + dist) // 2
            ans = max(ans, peak)
        
        return ans