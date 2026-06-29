class Solution:
    def partition(self, s: str) -> List[List[str]]:
        self.res = []
        self.helper(s)
        return self.res
    
    def helper(self, s: str, curr=[]) -> None:
        if not s:
            self.res.append(curr)
            return
        
        for i in range(1, len(s) + 1):
            if s[:i] == s[:i][::-1]:
                self.helper(s[i:], curr + [s[:i]])