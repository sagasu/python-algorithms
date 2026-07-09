from typing import List


class Solution:
    def pathExistenceQueries(
        self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]
    ) -> List[bool]:
        # nums is sorted non-decreasing. An edge exists between i and j when
        # |nums[i] - nums[j]| <= maxDiff. Because values are sorted, any path
        # must cross consecutive indices, so components are contiguous segments
        # split wherever the gap between neighbors exceeds maxDiff.
        component = [0] * n
        cid = 0
        for i in range(1, n):
            if nums[i] - nums[i - 1] > maxDiff:
                cid += 1
            component[i] = cid

        return [component[u] == component[v] for u, v in queries]
