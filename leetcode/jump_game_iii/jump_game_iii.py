from typing import List
from collections import deque


class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        n = len(arr)
        visited = set()
        q = deque([start])

        while q:
            i = q.popleft()
            if arr[i] == 0:
                return True
            if i in visited:
                continue
            visited.add(i)
            for ni in (i + arr[i], i - arr[i]):
                if 0 <= ni < n and ni not in visited:
                    q.append(ni)

        return False
