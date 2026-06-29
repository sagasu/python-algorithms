class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        N = len(nums)
        seen = set()
        duplicate = None

        total = 0
        for x in nums:
            if x in seen:
                duplicate = x
            else:
                total += x
                seen.add(x)

        return [duplicate, (N * (N + 1)) // 2- total]