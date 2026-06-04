from typing import List


class Solution:
    def closetTarget(self, words: List[str], target: str, startIndex: int) -> int:
        n = len(words)
        ans = float('inf')
        for i, w in enumerate(words):
            if w == target:
                d = abs(i - startIndex)
                ans = min(ans, min(d, n - d))
        return -1 if ans == float('inf') else ans
