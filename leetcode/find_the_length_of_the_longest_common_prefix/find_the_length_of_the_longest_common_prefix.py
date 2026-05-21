from typing import List


class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        # Store all numeric prefixes of arr1 numbers in a set
        prefixes = set()
        for n in arr1:
            s = str(n)
            for i in range(1, len(s) + 1):
                prefixes.add(s[:i])

        ans = 0
        for n in arr2:
            s = str(n)
            for i in range(1, len(s) + 1):
                if s[:i] in prefixes:
                    ans = max(ans, i)

        return ans
