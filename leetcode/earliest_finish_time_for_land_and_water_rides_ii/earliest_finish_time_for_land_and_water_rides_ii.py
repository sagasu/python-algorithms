from typing import List


class Solution:
    def earliestFinishTime(
        self,
        landStartTime: List[int],
        landDuration: List[int],
        waterStartTime: List[int],
        waterDuration: List[int],
    ) -> int:
        def calc(a1, t1, a2, t2) -> int:
            # Best first ride: minimum end time across all rides in category 1
            min_end = min(a + t for a, t in zip(a1, t1))
            # Best second ride: start at max(min_end, open_time) + duration
            return min(max(a, min_end) + t for a, t in zip(a2, t2))

        # Try both orderings: land first, or water first
        return min(
            calc(landStartTime, landDuration, waterStartTime, waterDuration),
            calc(waterStartTime, waterDuration, landStartTime, landDuration),
        )
