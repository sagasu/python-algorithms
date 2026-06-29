class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum = collections.Counter()
        prefix_sum[0] = 1
        
        cnt = s = 0
        for n in nums:
            s += n
             # if none, counter returns '0', so its ok to always just add.
            cnt += prefix_sum[s-k]
            prefix_sum[s] += 1
        
        return cnt