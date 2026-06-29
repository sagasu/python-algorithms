class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        return len([[x, t := t[t.index(x) + 1:]][0] for x in s if x in t]) == len(s)