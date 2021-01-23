class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if set(word1) != set(word2):
            return False

        f1 = collections.Counter(word1)
        f2 = collections.Counter(word2)

        f1v = f1.values()
        f2v = f2.values()

        f1v.sort()
        f2v.sort()

        for v1, v2 in zip(f1v, f2v):
            if v1 != v2:
                return False

        return True

