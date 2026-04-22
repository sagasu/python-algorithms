from typing import List


class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        def within_two(w, d):
            return sum(a != b for a, b in zip(w, d)) <= 2

        return [q for q in queries if any(within_two(q, d) for d in dictionary)]
