import heapq
from typing import List


class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], labels: str, k: int) -> int:
        """Dijkstra on (node, trailing identical-label run); skip hops that would exceed k."""
        graph = [[] for _ in range(n)]
        for u, v, w in edges:
            graph[u].append((v, w))

        inf = 10**18
        dist = [[inf] * (k + 1) for _ in range(n)]
        dist[0][1] = 0
        heap = [(0, 0, 1)]  # cost, node, run length of labels ending at node

        while heap:
            cost, u, run = heapq.heappop(heap)
            if cost != dist[u][run]:
                continue
            if u == n - 1:
                return cost
            last = labels[u]
            for v, w in graph[u]:
                nxt = run + 1 if labels[v] == last else 1
                if nxt > k:
                    continue
                ncost = cost + w
                if ncost < dist[v][nxt]:
                    dist[v][nxt] = ncost
                    heapq.heappush(heap, (ncost, v, nxt))
        return -1


if __name__ == "__main__":
    sol = Solution()
    tests = [
        (3, [[0, 1, 1], [1, 2, 1], [0, 2, 3]], "aab", 1, 3),
        (3, [[0, 1, 1], [1, 2, 1], [0, 2, 3]], "aab", 2, 2),
        (3, [[0, 1, 1], [1, 2, 1]], "aaa", 2, -1),
    ]
    failed = False
    for n, edges, labels, k, expected in tests:
        got = sol.shortestPath(n, edges, labels, k)
        if got == expected:
            print("OK")
        else:
            print("FAIL")
            failed = True
    if failed:
        raise SystemExit(1)
