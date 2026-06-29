class Solution:
    def __init__(self):
        self.row = "0"

    def kthGrammar(self, n: int, k: int) -> int:
        if(n == 1):
            return int(self.row[k-1])
        
        newRow = ""
        for element in self.row:
            newRow += "01" if element == "0" else "10"

        self.row = newRow
        return self.kthGrammar(n-1, k)
    
print(Solution().kthGrammar(3,1) == 0)
print(Solution().kthGrammar(3,2) == 1)
print(Solution().kthGrammar(3,3) == 1)
print(Solution().kthGrammar(3,4) == 0)
print(Solution().kthGrammar(1,1) == 0)
print(Solution().kthGrammar(30,434991989) == 0)