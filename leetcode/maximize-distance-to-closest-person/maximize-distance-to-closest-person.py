from typing import List

class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        previous, n, maxdistance = -1, len(seats), 0
        for i in range(n):
            if (seats[i]):
                maxdistance = max(maxdistance, i if previous == -1 else (i - previous) / 2)
                previous = i
        return int(max(maxdistance, n - 1 - previous))