from sortedcontainers import SortedList

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        sl = SortedList()
        nums.reverse()

        ans = []
        for x in nums:
            index = sl.bisect_right(-x)
            ans.append(len(sl) - index)
            sl.add(-x)
        ans.reverse()
        return ans