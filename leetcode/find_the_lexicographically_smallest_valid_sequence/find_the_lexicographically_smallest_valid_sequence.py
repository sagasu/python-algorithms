from typing import List


class Solution:
    def validSequence(self, word1: str, word2: str) -> List[int]:
        """
        Find the lex-smallest strictly increasing index sequence in word1 whose
        picked characters form a string almost-equal to word2 (at most one change).

        Approach:
        1. Greedily match word2 as a subsequence of word1 from the right.
           last[j] = index used for word2[j] in that rightmost exact match.
           last[j..] is therefore the rightmost way to match suffix word2[j:].
        2. Scan left-to-right building the lex-smallest answer:
           - Prefer an exact match for word2[j].
           - On mismatch, use our one allowed change at the earliest safe index:
             safe iff the remaining suffix word2[j+1:] still has a rightmost
             match entirely after i (i < last[j+1]), or j is the last char.
        """
        m = len(word2)
        last = [-1] * m

        i, j = len(word1) - 1, m - 1
        while i >= 0 and j >= 0:
            if word1[i] == word2[j]:
                last[j] = i
                j -= 1
            i -= 1

        ans: List[int] = []
        can_skip = True
        j = 0
        for i, c in enumerate(word1):
            if j == m:
                break
            if c == word2[j]:
                ans.append(i)
                j += 1
            elif can_skip and (j == m - 1 or i < last[j + 1]):
                # Use the single allowed change here; rest must match exactly.
                can_skip = False
                ans.append(i)
                j += 1

        return ans if j == m else []


if __name__ == "__main__":
    sol = Solution()
    tests = [
        ("vbcca", "abc", [0, 1, 2]),
        ("bacdc", "abc", [1, 2, 4]),
        ("aaaaaa", "aaabc", []),
        ("abc", "ab", [0, 1]),
        ("xabc", "yabc", [0, 1, 2, 3]),
        ("cab", "xab", [0, 1, 2]),
        ("aabc", "abc", [0, 1, 3]),  # skip at index 1 is lex-smaller than exact [0,2,3]
        ("xbca", "abc", [0, 1, 2]),
    ]
    for word1, word2, expected in tests:
        got = sol.validSequence(word1, word2)
        status = "OK" if got == expected else "FAIL"
        print(f"{status}: word1={word1!r} word2={word2!r} -> {got} (expected {expected})")
