class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        N = len(edges)
        parent = list(x for x in range(N))

        def ufind(x):
            if parent[x] != x:
                parent[x] = ufind(parent[x])
            return parent[x]

        def uunion(a,b):
            ua = ufind(a)
            ub = ufind(b)

            parent[ua] = ub

        for u, v in edges:
            u -= 1
            v -= 1

            if ufind(u) == ufind(v):
                return [u + 1, v +1]
            uunion(u,v)
            