from typing import List
from functools import reduce
from operator import xor

MOD = 10**9 + 7


class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        for l, r, k, v in queries:
            for idx in range(l, r + 1, k):
                nums[idx] = nums[idx] * v % MOD
        return reduce(xor, nums)
