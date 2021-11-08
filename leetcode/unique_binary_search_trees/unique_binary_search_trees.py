class Solution:
    def numTrees(self, n):
            c = 1
            for i in range(1,n):
                #Catalan number
                c = c * 2 * (2 * i + 1) / (i + 2)
            return int(c)