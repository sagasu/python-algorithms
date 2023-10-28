class Solution:
    def countVisitedNodes(self, edges):
        n, dict1 = len(edges), defaultdict(list)

        indegree, dist = [0]*n, [0]*n

        for i,j in enumerate(edges):
            dict1[i].append(j)
            indegree[j] += 1

        stack, kahn = [], set()

        for i in range(n):
            if indegree[i] == 0:
                stack.append(i)
                kahn.add(i)

        while stack:
            node = stack.pop(0)

            for neighbor in dict1[node]:
                indegree[neighbor] -= 1 

                if indegree[neighbor] == 0:
                    stack.append(neighbor)
                    kahn.add(neighbor)

        cyclic_nodes = [i for i in set(range(n))-kahn]

        for i in cyclic_nodes:
            if dist[i] == 0:
                stk, visited = [i], set([i])

                while stk:
                    node = stk.pop()

                    for neighbor in dict1[node]:
                        if neighbor not in visited:
                            visited.add(neighbor)
                            stk.append(neighbor)

                for j in visited: dist[j] = len(visited)

        @lru_cache(None)
        def dfs(v):
            if dist[v] != 0: return dist[v]
            return 1 + dfs(edges[v])

        for i in kahn:
            dist[i] = dfs(i)

        return dist