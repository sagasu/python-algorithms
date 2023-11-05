from typing import List
from queue import Queue 

class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        x, y = arr[0], 1
        for i in range(1, len(arr)):
            if arr[i] > x:
                if i-y >= k:
                    return x
                else:
                    x, y = arr[i], i
        return x
    
print(Solution().getWinner([2,1,3,5,4,6,7],2) == 5)
print(Solution().getWinner([3,2,1],10) == 3)
print(Solution().getWinner([1,11,22,33,44,55,66,77,88,99],1000000000) == 99)
            