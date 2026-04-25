from typing import List
from bisect import bisect_left


class Solution:
    def maxDistance(self, side: int, points: List[List[int]], k: int) -> int:
        # Map each boundary point to a 1D perimeter position [0, 4*side)
        # Bottom: (0,0)->(side,0): x goes 0->side, pos = x  (but start at y=0, x=0)
        # Actually traverse: left edge up, top edge right, right edge down, bottom edge left
        # Standard CCW: bottom-left corner = 0
        # Left edge (x=0): y from 0 to side -> pos = y
        # Top edge (y=side): x from 0 to side -> pos = side + x
        # Right edge (x=side): y from side to 0 -> pos = 3*side - y
        # Bottom edge (y=0): x from side to 0 -> pos = 4*side - x
        nums = []
        for x, y in points:
            if x == 0:
                nums.append(y)
            elif y == side:
                nums.append(side + x)
            elif x == side:
                nums.append(3 * side - y)
            else:
                nums.append(4 * side - x)
        nums.sort()
        n = len(nums)
        total = 4 * side

        def check(lo: int) -> bool:
            # Try each point as the starting point, greedily pick k points
            # with consecutive perimeter distance >= lo (circular)
            for start in nums:
                end = start + total - lo  # last valid position (circular)
                cur = start
                ok = True
                for _ in range(k - 1):
                    j = bisect_left(nums, cur + lo)
                    if j == n or nums[j] > end:
                        ok = False
                        break
                    cur = nums[j]
                if ok:
                    return True
            return False

        lo, hi = 1, side
        while lo < hi:
            mid = (lo + hi + 1) >> 1
            if check(mid):
                lo = mid
            else:
                hi = mid - 1
        return lo
