class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        N = len(word1)
        M = len(word2)

        has_cache = [[False] * (M+1) for _ in range(N+1)]
        cache = [[float("inf")] * (M+1) for _ in range(N+1)]

        def minD(index1, index2):
            if index1 == N and index2 == M:
                return 0
            if index1 == N:
                return minD(index1, index2 + 1) + 1
            if index2 == M:
                return minD(index1 + 1, index2) + 1
            if has_cache[index1][index2]:
                return cache[index1][index2]

            mn = float("inf")
            if word1[index1] == word2[index2]:
                mn = min(mn, minD(index1+1, index2 +1))
            mn = min(mn, minD(index1 + 1, index2) + 1)
            mn = min(mn, minD(index1, index2 + 1) + 1)
            has_cache[index1][index2] = True
            cache[index1][index2] = mn
            return mn
        return minD(0,0)

        