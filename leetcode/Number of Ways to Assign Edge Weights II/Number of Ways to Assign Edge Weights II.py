from typing import List

class Solution:
    def assignEdgeWeights(self, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        n = len(edges) + 1
        MOD = 10**9 + 7
        LOG = 17  # 2^17 > 1e5
        
        graph = [[] for _ in range(n + 1)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        depth = [0] * (n + 1)
        parent = [[-1] * (n + 1) for _ in range(LOG)]
        
        # DFS to compute depth and parent[0]
        def dfs(u: int, p: int):
            parent[0][u] = p
            for v in graph[u]:
                if v != p:
                    depth[v] = depth[u] + 1
                    dfs(v, u)
        
        dfs(1, -1)
        
        # Build binary lifting table
        for k in range(1, LOG):
            for v in range(1, n + 1):
                if parent[k - 1][v] != -1:
                    parent[k][v] = parent[k - 1][parent[k - 1][v]]
        
        def get_lca(u: int, v: int) -> int:
            if depth[u] < depth[v]:
                u, v = v, u
            # Lift u to same depth as v
            diff = depth[u] - depth[v]
            k = 0
            while diff:
                if diff & 1:
                    u = parent[k][u]
                diff >>= 1
                k += 1
            if u == v:
                return u
            # Lift both u and v
            for k in range(LOG - 1, -1, -1):
                if parent[k][u] != parent[k][v]:
                    u = parent[k][u]
                    v = parent[k][v]
            return parent[0][u]
        
        def mod_pow(base: int, exp: int) -> int:
            res = 1
            base %= MOD
            while exp > 0:
                if exp & 1:
                    res = res * base % MOD
                base = base * base % MOD
                exp >>= 1
            return res
        
        ans = []
        for u, v in queries:
            if u == v:
                ans.append(0)
            else:
                lca = get_lca(u, v)
                dist = depth[u] + depth[v] - 2 * depth[lca]
                # Number of ways with odd number of 1's: 2^(dist-1)
                ans.append(mod_pow(2, dist - 1))
        
        return ans