class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        def getPrefix(nums):
            stack = [nums[0]]
            popped = False

            for x in nums[1:]:
                if len(stack) == 0:
                    break

                while len(stack) > 0 and stack[-1] > x:
                    stack.pop()
                    popped = True

                if not popped:
                    stack.append(x)

            return len(stack)
        
        prefixLen = getPrefix(nums)
        if prefixLen == len(nums):
            return 0

        suffixLen = getPrefix(list(-x for x in nums[::-1]))
        return len(nums) - prefixLen - suffixLen
                    