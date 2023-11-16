class Solution:
    def findDifferentBinaryString(self, nums):
        n, num_set = len(nums[0]), set(nums)

        def backtrack(idx,path):
            if len(path) == n:
                return None if path in num_set else path

            for i in range(idx,n):
                res = backtrack(i+1,path+"0") or backtrack(i+1,path+"1")
                if res: return res

        return backtrack(0,"")