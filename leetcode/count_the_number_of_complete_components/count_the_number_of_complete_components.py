from collections import defaultdict
from typing import List, Tuple


class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        # A connected component of size m is complete (a clique) iff it has
        # exactly m * (m - 1) / 2 edges. DFS counts nodes and the sum of
        # degrees in the component; sum of degrees equals 2 * edge_count.
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        visited = [False] * n

        def dfs(node: int) -> Tuple[int, int]:
            visited[node] = True
            nodes, degree_sum = 1, len(graph[node])
            for nei in graph[node]:
                if not visited[nei]:
                    n_nodes, n_deg = dfs(nei)
                    nodes += n_nodes
                    degree_sum += n_deg
            return nodes, degree_sum

        ans = 0
        for i in range(n):
            if not visited[i]:
                nodes, degree_sum = dfs(i)
                # degree_sum == 2 * edges, complete iff edges == nodes*(nodes-1)/2
                if degree_sum == nodes * (nodes - 1):
                    ans += 1
        return ans
