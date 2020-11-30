from sortedcontainers import SortedList

class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        ADD_BUILDING = 0
        REMOVE_BUILDING = 1

        unique_events = set()
        events = collections.defaultdict(list)

        for left, right, height in buildings:
            unique_events.add(left)
            unique_events.add(right)

            events[left].append((ADD_BUILDING, height))
            events[right].append((REMOVE_BUILDING, height))

        current_heights = SortedList()
        current_heights.add(0)
        results = []

        for x in sorted(list(unique_events)):
            for event, height in events[x]:
                if event == ADD_BUILDING:
                    current_heights.add(height)
                else:
                    current_heights.remove(height)
            if len(results) == 0 or results[-1][1] != current_heights[-1]:
                results.append([x, current_heights[-1]])
        return results
