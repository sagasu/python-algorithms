class Solution:
  def countPalindromicSubsequence(self, s: str) -> int:
    return sum(len(set(s[s.find(char)+1:s.rfind(char)])) for char in set(s))