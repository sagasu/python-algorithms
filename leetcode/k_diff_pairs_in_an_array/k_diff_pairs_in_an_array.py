class Solution:
	def findPairs(self, nums: List[int], k: int) -> int:
		from collections import Counter
		cnt = Counter(nums)
		s = set(nums)
		res = 0
		if k == 0:
			for i in cnt:
				if cnt[i] > 1:
					res += 1
			return res
		else:
			for i in s:
				if i + k in s:
					res += 1
			return res