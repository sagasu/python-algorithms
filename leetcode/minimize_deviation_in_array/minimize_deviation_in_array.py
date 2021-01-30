class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        heap = []
        inf = 1000000000
        smallest = inf
        
        for x in nums:
            if x % 2 == 0:
                hepq.heappush(heap, -x)
                smallest = min(smallest, x)

            else:
                heapq.heappush(heap, -(x * 2))
                smallest = min(smallest, x * 2)

        best = inf
        while len(heap) > 0:
            largest = -heap[0]

            heapq.heappop(heap)
            best = min(best, largest - smallest)

            if largest % 2 ==1:
                break
            else:
                heapq.heappush(heap, -(largest // 2))
                smallest = min(smallest, largest //2)

        return best