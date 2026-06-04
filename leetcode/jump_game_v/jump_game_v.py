from typing import List
from functools import cache


class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        n = len(arr)

        @cache
        def dp(i: int) -> int:
            best = 1  # can always visit at least the current index
            # Jump right
            for j in range(i + 1, min(i + d + 1, n)):
                if arr[j] >= arr[i]:
                    break  # blocked
                best = max(best, 1 + dp(j))
            # Jump left
            for j in range(i - 1, max(i - d - 1, -1), -1):
                if arr[j] >= arr[i]:
                    break  # blocked
                best = max(best, 1 + dp(j))
            return best

        return max(dp(i) for i in range(n))
