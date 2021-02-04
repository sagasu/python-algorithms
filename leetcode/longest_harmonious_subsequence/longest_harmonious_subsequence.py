class Solution:
    def findLHS(self, nums: List[int]) -> int:
        best = 0
        count = collections.Counter(nums)

        for x in count.keys():
            if x + 1 in count:
                best = max(best, count[x] + count[x + 1])

        return best