from typing import List
from collections import defaultdict


class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        def check(g: List[List[int]]) -> bool:
            m, n = len(g), len(g[0])
            s1, s2 = 0, 0
            cnt1, cnt2 = defaultdict(int), defaultdict(int)

            # Start with everything in the bottom section
            for row in g:
                for x in row:
                    s2 += x
                    cnt2[x] += 1

            # Try each horizontal cut after row i (top = rows 0..i, bottom = rows i+1..m-1)
            for i, row in enumerate(g[: m - 1]):
                for x in row:
                    s1 += x
                    s2 -= x
                    cnt1[x] += 1
                    cnt2[x] -= 1

                if s1 == s2:
                    return True

                if s1 < s2:
                    # Need to remove a cell of value `diff` from the bottom section
                    diff = s2 - s1
                    if cnt2[diff]:
                        bottom_rows = m - i - 1
                        # Removable if bottom has >1 row and >1 col (any border cell works),
                        # or bottom is a single row (only corner cells keep it connected),
                        # or grid is a single column (only first or last cell of bottom)
                        if (bottom_rows > 1 and n > 1) \
                           or (i == m - 2 and (g[i+1][0] == diff or g[i+1][-1] == diff)) \
                           or (n == 1 and (g[i+1][0] == diff or g[-1][0] == diff)):
                            return True
                else:
                    # Need to remove a cell of value `diff` from the top section
                    diff = s1 - s2
                    if cnt1[diff]:
                        top_rows = i + 1
                        if (top_rows > 1 and n > 1) \
                           or (i == 0 and (g[0][0] == diff or g[0][-1] == diff)) \
                           or (n == 1 and (g[0][0] == diff or g[i][0] == diff)):
                            return True

            return False

        # Check horizontal cuts, then vertical cuts (via transpose)
        return check(grid) or check(list(zip(*grid)))
