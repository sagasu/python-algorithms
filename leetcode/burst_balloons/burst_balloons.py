class Solution:
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = [1] + nums + [1]
        n = len(nums)
        dp = [[0] * n for i in range(n)]
        for j in range(2, n):
            for i in range(j-2, -1, -1):
                for k in range(i+1,j):
                    dp[i][j] = max(dp[i][j], dp[i][k] + dp[k][j] + nums[i]*nums[j]*nums[k])
        return dp[0][-1]