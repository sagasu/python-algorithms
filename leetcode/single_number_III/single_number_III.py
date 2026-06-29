class Solution(object):
    def singleNumber(self, nums):
        diff = reduce(lambda x, y: x ^ y, nums, 0)
        diff &= -diff
        res = [0, 0]
        for num in nums:
            res[num & diff == 0] ^= num
        return res