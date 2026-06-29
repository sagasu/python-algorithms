class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        unique = set(s)
        for i, element in enumerate(unique):
            if element.swapcase() not in unique:
                return max(map(self.longestNiceSubstring, [s[:i], s[i+1:]]), key=len)
        return s

print(Solution().longestNiceSubstring("bB") == "bB")