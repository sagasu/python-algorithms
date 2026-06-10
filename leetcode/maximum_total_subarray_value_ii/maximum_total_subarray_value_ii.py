import heapq
import math

class Solution:
    def maxTotalValue(self, nums: list[int], k: int) -> int:
        n = len(nums)
        if n == 0 or k == 0:
            return 0
        
        # Precompute log
        log = [0] * (n + 1)
        for i in range(2, n + 1):
            log[i] = log[i // 2] + 1
        
        # Sparse Table for Range Max Query
        st_max = [[0] * (log[n] + 1) for _ in range(n)]
        for i in range(n):
            st_max[i][0] = nums[i]
        for j in range(1, log[n] + 1):
            for i in range(n - (1 << j) + 1):
                st_max[i][j] = max(st_max[i][j-1], st_max[i + (1 << (j-1))][j-1])
        
        # Sparse Table for Range Min Query
        st_min = [[0] * (log[n] + 1) for _ in range(n)]
        for i in range(n):
            st_min[i][0] = nums[i]
        for j in range(1, log[n] + 1):
            for i in range(n - (1 << j) + 1):
                st_min[i][j] = min(st_min[i][j-1], st_min[i + (1 << (j-1))][j-1])
        
        def query_max(l: int, r: int) -> int:
            if l > r:
                return float('-inf')
            length = r - l + 1
            j = log[length]
            return max(st_max[l][j], st_max[r - (1 << j) + 1][j])
        
        def query_min(l: int, r: int) -> int:
            if l > r:
                return float('inf')
            length = r - l + 1
            j = log[length]
            return min(st_min[l][j], st_min[r - (1 << j) + 1][j])
        
        # Max-heap: (-value, left, right)
        pq = []
        for l in range(n):
            val = query_max(l, n-1) - query_min(l, n-1)
            heapq.heappush(pq, (-val, l, n-1))
        
        total = 0
        for _ in range(k):
            if not pq:
                break
            neg_val, l, r = heapq.heappop(pq)
            total += -neg_val
            if l < r:
                nr = r - 1
                nval = query_max(l, nr) - query_min(l, nr)
                heapq.heappush(pq, (-nval, l, nr))
        
        return total