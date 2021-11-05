class Solution(object):
    def arrangeCoins(self, n):
        m = 2 * n
        val = int(math.sqrt(m))
        while val * (val + 1) > 2*n:
            val -= 1
        return val