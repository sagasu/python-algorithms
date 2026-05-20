from typing import List


class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n = len(A)
        seen = [False] * (n + 1)  # values are 1..n (permutation)
        common = 0
        ans = []

        for a, b in zip(A, B):
            # Add a: if already seen from B side, it's now common
            if seen[a]:
                common += 1
            else:
                seen[a] = True

            # Add b: if already seen from A side (or just added above), it's common
            if seen[b]:
                common += 1
            else:
                seen[b] = True

            ans.append(common)

        return ans
