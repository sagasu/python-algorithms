class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        last = -1000000

        for index, x in enumerate(nums):
            if x == 1:
                if index - last -1 < k:
                    return False
                last = index
        return True