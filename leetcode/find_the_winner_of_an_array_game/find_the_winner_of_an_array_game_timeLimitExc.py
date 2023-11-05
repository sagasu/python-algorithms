from typing import List
from queue import Queue 

class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        queue = Queue()
        for element in arr[1:]:
            queue.put(element)

        curr = arr[0]
        count = 0
        while queue.not_empty:
            if count >= k:
                return curr
            
            first = queue.get()
            if(curr > first):
                count+=1
                queue.put(first)
            else:
                count = 1
                queue.put(curr)
                curr = first
        return 0
    
print(Solution().getWinner([2,1,3,5,4,6,7],2) == 5)
print(Solution().getWinner([3,2,1],10) == 3)
print(Solution().getWinner([1,11,22,33,44,55,66,77,88,99],1000000000) == 99)
            