from typing import List


class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        ans = []
        last = 0
        for val in pref:
            ans.append(last ^ val)
            last ^= ans[-1]
        return ans