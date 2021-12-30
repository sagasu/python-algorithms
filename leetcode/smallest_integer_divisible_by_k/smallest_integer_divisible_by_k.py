class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        n = 1
        while n<k: 
            n = 10*n + 1

        rm = set()
        while True:
            if n%k==0:
                return len(str(n))
            if n%k in rm:
                retu/rn -1
            rm.add(n%k)
            n = 10*n + 1