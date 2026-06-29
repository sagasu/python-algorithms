class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        snums = set(nums)

        def get_longest_increasing(x):
            ans = 1
            if x + 1 in snums:
                ans = 1 + get_longest_increasing(x + 1)
            return ans
        
        ans = 0
        for x in nums:
            if x - 1 not in snums:
                ans = max(ans, get_longest_increasing(x))

        return ans