from typing import List
from sortedcontainers import SortedList
import itertools


class FenwickTree:
    """Max Fenwick Tree — supports point update (maximize) and prefix max query."""
    def __init__(self, n: int):
        self.vals = [0] * (n + 1)

    def maximize(self, i: int, val: int) -> None:
        while i < len(self.vals):
            self.vals[i] = max(self.vals[i], val)
            i += i & -i

    def query(self, i: int) -> int:
        res = 0
        while i > 0:
            res = max(res, self.vals[i])
            i -= i & -i
        return res


class Solution:
    def getResults(self, queries: List[List[int]]) -> List[bool]:
        n = min(50000, len(queries) * 3)
        tree = FenwickTree(n + 1)
        # Start with all obstacles (type 1 queries) inserted, plus sentinels 0 and n
        obstacles = SortedList([0, n])

        for q in queries:
            if q[0] == 1:
                obstacles.add(q[1])

        # Initialize tree with gap sizes between consecutive obstacles
        for x1, x2 in itertools.pairwise(obstacles):
            tree.maximize(x2, x2 - x1)

        # Process queries in reverse (type 1 becomes removal)
        ans = []
        for q in reversed(queries):
            t, x = q[0], q[1]
            if t == 1:
                # Remove obstacle x; merge its two gaps into one
                i = obstacles.index(x)
                nxt = obstacles[i + 1]
                prv = obstacles[i - 1]
                obstacles.remove(x)
                tree.maximize(nxt, nxt - prv)
            else:
                sz = q[2]
                # Find the nearest obstacle to the left of x
                i = obstacles.bisect_right(x)
                prv = obstacles[i - 1]
                # Can place block of size sz if:
                # 1. Gap between prv and x is >= sz, OR
                # 2. Max gap ending at or before prv is >= sz
                ans.append(tree.query(prv) >= sz or x - prv >= sz)

        return ans[::-1]
