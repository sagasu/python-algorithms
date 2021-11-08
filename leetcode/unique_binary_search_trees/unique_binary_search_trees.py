class Solution:
    def numTrees(self, n):
        if n == 0: return 1
        res = 0
        for i in range(1, n+1):
            res += self.numTrees(i-1)*self.numTrees(n-i)
        return res