class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        edges = collections.defaultdict(list)

        for a, b in connections:
            edges[a].append(b)
            edges[b].append(a)

        t = 0
        inf = float("inf")
        parent = [-1]*n
        visited = [False]*n
        first_visited = [inf]*n
        lowest = [inf]*n
        ans = []

        def dfs(current):
            visited[current] = True

            nonlocal t
            first_visited[current] = t
            lowest[current] = t
            t+=1

            for x in edges[current]:
                if not visited[x]:
                    parent[x] =current
                    dfs(x)

                    lowest[current]=min(lowest[current], lowest[x])
                    if lowest[x] > first_visited[current]:
                        ans.append((x, current))

                elif x != parent[current]:
                    lowest[current] = min(lowest[current], first_visited[x])

        for x in range(n):
            if not visited[x]:
                dfs(x)

        return ans