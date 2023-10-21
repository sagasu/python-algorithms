class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        dp = [n for n in nums]
        res = float('-inf')
        dq = collections.deque()
        for i in range(len(nums)):
            while dq and (dq[0] < i-k or dp[dq[0]] <=0):
                dq.popleft()
            if dq:
                dp[i] = dp[dq[0]] + nums[i] 
            res = max(res,dp[i])
            
            while dq and dp[dq[-1]] < dp[i]:
                dq.pop()
            dq.append(i)    
        return res