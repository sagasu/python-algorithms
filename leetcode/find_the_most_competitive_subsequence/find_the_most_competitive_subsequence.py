class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        N = len(nums)
        heap = []
        ans = []
        lastSeenIndex = -1

        for index in range(N - k + 1):
            heapq.heappush(heap, (nums[index], index))
        index = N - k + 1

        for _ in range(k):
            while heap[0][1] <= lastSeenIndex:
                heapq.heappop(heap)

            x, lastIndex = heap[0]
            lastSeenIndex = lastIndex
            ans.append(x)

            if index < N:
                heapq.heappush(heap, (nums[index], index))
                index += 1
        
        return ans