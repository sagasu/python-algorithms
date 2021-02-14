class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        N = len(graph)

        WHITE = 0
        RED = 1
        BLUE = 2
        colors = [WHITE] * N

        def goColor(start):
            q = collections.deque()
            colors[start] = RED
            q.append((RED, start))

            while len(q) > 0:
                currentColor, x = q.popleft()
                nextColor = (RED if currentColor == BLUE else BLUE)

                for v in graph[x]:
                    if colors[v] == WHITE:
                        colors[v] = nextColor
                        q.append((nextColor, v))

                    elif colors[v] != nextColor:
                        return False
            return True

        for x in range(N):
            if colors[x] == WHITE:
                if not goColor(x):
                    return False

        return True