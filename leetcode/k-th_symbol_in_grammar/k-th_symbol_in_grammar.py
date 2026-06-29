class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        return 1 if n and self.kthGrammar(n-1, (k+1) // 2) == k & 1 else 0
    
print(Solution().kthGrammar(3,1) == 0)
print(Solution().kthGrammar(3,2) == 1)
print(Solution().kthGrammar(3,3) == 1)
print(Solution().kthGrammar(3,4) == 0)
print(Solution().kthGrammar(1,1) == 0)
print(Solution().kthGrammar(30,434991989) == 0)