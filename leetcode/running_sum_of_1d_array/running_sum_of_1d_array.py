class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        ans = [0]
        for _ in rums:
            ans.append(ans[-1] + _)
        return ans[1:]