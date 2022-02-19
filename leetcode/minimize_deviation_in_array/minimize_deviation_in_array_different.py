class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        nums = [n if n%2==0 else 2*n for n in nums]
        MIN = min(nums)
        dq = []
        for n in nums: heapq.heappush(dq, -n)
        res = -dq[0]-MIN
        while -dq[0]%2==0:
            n = heapq.heappop(dq)
            heapq.heappush(dq, n//2)
            MIN = min(MIN, -n//2)
            res = min(res, -dq[0]-MIN)
        return res