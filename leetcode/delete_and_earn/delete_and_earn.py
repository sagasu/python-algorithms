class Solution:
	def deleteAndEarn(self, nums: List[int]) -> int:
		count_frequency = defaultdict(int)
		max_number = max(nums)

		for num in nums: count_frequency[num] = count_frequency[num] + num

		dp = [0]*(max_number + 1)
		dp[1] = count_frequency[1]

		for j in range(2,len(dp)):	dp[j] = max(dp[j-1], dp[j-2] + count_frequency[j])

		return dp[max_number]