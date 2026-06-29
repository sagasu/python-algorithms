from collections import deque
from typing import List

class Solution:
    def assignEdgeWeights(self, edges: List[List[int]]) -> int:
        MOD = 10**9 + 7
        n = len(edges) + 1
        if n == 1:
            return 0  # No edges
        
        # Build adjacency list
        graph = [[] for _ in range(n + 1)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        # BFS to find max depth (number of edges) from root 1
        queue = deque([1])
        visited = [False] * (n + 1)
        visited[1] = True
        max_depth = 0
        
        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                for nei in graph[node]:
                    if not visited[nei]:
                        visited[nei] = True
                        queue.append(nei)
                        max_depth = max(max_depth, 1)  # We'll track level properly below
        
        # Proper level-by-level BFS for max depth
        queue = deque([1])
        visited = [False] * (n + 1)
        visited[1] = True
        max_depth = 0
        
        while queue:
            level_size = len(queue)
            for _ in range(level_size):
                node = queue.popleft()
                for nei in graph[node]:
                    if not visited[nei]:
                        visited[nei] = True
                        queue.append(nei)
            if queue:  # If there's next level
                max_depth += 1
        
        # Number of ways: 2^(max_depth - 1) % MOD if max_depth >= 1
        if max_depth == 0:
            return 0
        return pow(2, max_depth - 1, MOD)