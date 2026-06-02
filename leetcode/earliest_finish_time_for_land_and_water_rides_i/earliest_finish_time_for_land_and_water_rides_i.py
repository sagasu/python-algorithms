from typing import List


class Solution:
    def minFinishTime(
        self,
        landStartTime: List[int],
        landDuration: List[int],
        waterStartTime: List[int],
        waterDuration: List[int],
    ) -> int:
        ans = float('inf')

        for ls, ld in zip(landStartTime, landDuration):
            for ws, wd in zip(waterStartTime, waterDuration):
                # Order 1: land then water
                land_end = ls + ld
                water_start = max(land_end, ws)
                finish1 = water_start + wd

                # Order 2: water then land
                water_end = ws + wd
                land_start = max(water_end, ls)
                finish2 = land_start + ld

                ans = min(ans, finish1, finish2)

        return ans
