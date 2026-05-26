class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        chars = set(word)
        return sum(c in chars and c.upper() in chars for c in 'abcdefghijklmnopqrstuvwxyz')
