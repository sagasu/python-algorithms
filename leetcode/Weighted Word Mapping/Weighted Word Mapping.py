from typing import List
import string

class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        ans = []
        ascii_lowercase = string.ascii_lowercase
        for w in words:
            s = sum(weights[ord(c) - ord('a')] for c in w)
            mapped = ascii_lowercase[25 - (s % 26)]
            ans.append(mapped)
        return ''.join(ans)