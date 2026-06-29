class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        strengthHeap = []

        for index, row in enumerate(mat):
            oneCount = row.count(1)

            heapq.heappush(strengthHeap, (-oneCount, -index))
            if len(strengthHeap) > k:
                heapq.heappop(strengthHeap)

        results = []
        while len(strengthHeap) > 0:
            topOneCount, topIndex = heapq.heappop(strengthHeap)
            topIndex *= -1
            results.append(topIndex)

        results.reverse()
        return results