class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        h = []

        for index, (x,y) in enumerate(zip(heights, heights[1:])):
            if x >= y:
                continue

            delta = y - x
            heapq.heappush(h, delta)

            while len(h) > ladders:
                bricks -= heapq.heappop(h)

            if bricks < 0:
                return index
        return len(heights) - 1