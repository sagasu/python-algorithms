
from sortedcontainers import SortedList

class MedianFinder:

    def __init__(self):
        self.srr = SortedList()  
        self.n = 0
    def addNum(self, x: int) -> None:
        self.srr.add(x)
        self.n += 1
    def findMedian(self) -> float:
        if self.n%2==1:
            return self.srr[self.n//2]
        else:
            return (self.srr[self.n//2]+self.srr[self.n//2-1])/2
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()