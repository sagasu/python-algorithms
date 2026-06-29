class NumArray:

    def __init__(self, nums: List[int]):
        N = len(nums)
        self.BIT = BIT(N)
        self.nums = nums

        for index, x in enumerate(nums):
            self.BIT.increase(index, x)

    def update(self, index: int, val: int) -> None:
        delta = val - self.nums[index]
        self.BIT.increase(index, delta)
        self.nums[index]=val

    def sumRange(self, left: int, right: int) -> int:
        return self.BIT.sumByRange(left, right)

class BIT:
    def __init__(self, N: int):
        self.N = N
        self.elements = [0] * (N + 1)

    def increase(self, index:int, delta: int):
        while index < self.N:
            self.elements[index] += delta
            index |= index + 1
        
    def sum(self, index: int):
        total = 0

        while index >= 0:
            total += self.elements[index]
            index &= index + 1
            index -= 1
            
        return total

    def sumByRange(self, left: int, right: int):
        return self.sum(right) - self.sum(left - 1)
        

            

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)