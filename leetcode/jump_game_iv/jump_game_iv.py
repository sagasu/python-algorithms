from typing import List
from collections import defaultdict, deque


class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)
        if n == 1:
            return 0

        # Group indices by value for same-value jumps
        val_to_idx = defaultdict(list)
        for i, v in enumerate(arr):
            val_to_idx[v].append(i)

        visited = {0}
        q = deque([0])
        steps = 0

        while q:
            steps += 1
            for _ in range(len(q)):
                i = q.popleft()
                # Adjacent jumps
                for ni in (i - 1, i + 1):
                    if ni == n - 1:
                        return steps
                    if 0 <= ni < n and ni not in visited:
                        visited.add(ni)
                        q.append(ni)
                # Same-value teleportation
                for ni in val_to_idx.pop(arr[i], []):
                    if ni == n - 1:
                        return steps
                    if ni not in visited:
                        visited.add(ni)
                        q.append(ni)

        return -1
