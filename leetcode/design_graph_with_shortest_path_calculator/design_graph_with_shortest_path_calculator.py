class Graph:

    def __init__(self, n: int, edges: List[List[int]]):
        self.g = defaultdict(list)
        for u,v,w in edges:
            self.g[u].append((v, w))

    def addEdge(self, edge: List[int]) -> None:
        u, v, w = edge
        self.g[u].append((v, w))

    def shortestPath(self, node1: int, node2: int) -> int:
        heap = [(0, node1)]
        costs = defaultdict(lambda: float('inf'))
        costs[node1] = 0

        while heap:
            cost, node = heappop(heap)
            if cost > costs[node]:
                continue
            if node == node2:
                return cost
            for neighbour, node_neigh_cost in self.g[node]:
                to_neigh_cost = cost + node_neigh_cost
                if to_neigh_cost < costs[neighbour]:
                    costs[neighbour] = to_neigh_cost
                    heappush(heap, (to_neigh_cost, neighbour))
        
        return -1

# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)