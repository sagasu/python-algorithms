from typing import List


class Solution:
    def findTheString(self, lcp: List[List[int]]) -> str:
        n = len(lcp)
        word = [''] * n
        c = ord('a')

        # Phase 1: greedily assign smallest letters
        for i in range(n):
            if word[i]:
                continue
            if c > ord('z'):
                return ""
            ch = chr(c)
            c += 1
            # All positions j where lcp[i][j] > 0 must share the same character as i
            for j in range(i, n):
                if lcp[i][j] > 0:
                    word[j] = ch

        # Phase 2: validate — recompute lcp from word and compare
        # lcp[i][j] = 1 + lcp[i+1][j+1] if word[i] == word[j], else 0
        # Check bottom-up (i and j from n-1 down to 0)
        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if word[i] == word[j]:
                    expected = 1 + (lcp[i + 1][j + 1] if i + 1 < n and j + 1 < n else 0)
                else:
                    expected = 0
                if lcp[i][j] != expected:
                    return ""

        return ''.join(word)
