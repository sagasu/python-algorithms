class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        dict1 = collections.defaultdict(list)

        for i in range(len(routes)):
            for j in routes[i]:
                dict1[j].append(i)

        stack, visited = [(0,source)], set()

        while stack:
            total, bus_stop = stack.pop(0)

            if bus_stop == target:
                return total

            for bus in dict1[bus_stop]:
                if bus not in visited:
                    for s in routes[bus]:
                        stack.append((total+1,s))
                    visited.add(bus)

        return -1