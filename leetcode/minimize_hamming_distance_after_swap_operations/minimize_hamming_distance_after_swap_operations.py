from typing import List
from collections import Counter


class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        n = len(source)

        # Union-Find
        parent = list(range(n))

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(a, b):
            parent[find(a)] = find(b)

        for a, b in allowedSwaps:
            union(a, b)

        # Group indices by their root
        groups = {}
        for i in range(n):
            r = find(i)
            groups.setdefault(r, []).append(i)

        # For each group, count how many positions can be matched
        ans = 0
        for indices in groups.values():
            src_count = Counter(source[i] for i in indices)
            tgt_count = Counter(target[i] for i in indices)
            # Matched = sum of min(src_count[v], tgt_count[v]) for each value v
            matched = sum(min(src_count[v], tgt_count[v]) for v in src_count)
            ans += len(indices) - matched

        return ans
