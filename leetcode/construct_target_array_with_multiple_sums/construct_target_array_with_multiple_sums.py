class Solution:
    def isPossible(self, target: List[int]) -> bool:
        total = sum(target)

        h = list(-x for x in target)
        heapq.heapify(h)

        while True:
            biggest = -heapq.heappop(h)
            if biggest == 1:
                return True
            if total == biggest:
                return False
            if total - biggest == 1:
                return True
            prev = total %(total - biggest)
            if prev >= biggest:
                return False
            total = total - biggest + prev
            if prev <= 0:
                return False
            heapq.heappush(h, -prev)
        return True
        