from typing import List


class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        # Rank = 1-based index among sorted unique values.
        rank = {v: i for i, v in enumerate(sorted(set(arr)), 1)}
        return [rank[x] for x in arr]
