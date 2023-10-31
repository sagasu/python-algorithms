from typing import List


class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        arr.sort()
        arr.sort(key=self.countOnes)
        
        return arr
    
    def countOnes(self, e):
        return format(e, 'b').count("1")
    

print(Solution().countOnes(4))
print(Solution().countOnes(3))
print(Solution().countOnes(2))
print(Solution().countOnes(1))
print(Solution().countOnes(0))

print(Solution().sortByBits([0,1,2,3,4,5,6,7,8]) == [0,1,2,4,8,3,5,6,7])
print(Solution().sortByBits([1024,512,256,128,64,32,16,8,4,2,1]) == [1,2,4,8,16,32,64,128,256,512,1024])