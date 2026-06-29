class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        N1, N2 = len(word1), len(word2)
        INF = 10 ** 20

        has_cache = [[False] * (N2 +1) for _ in range(N1 + 1)]
        cache = [[None] * (N2+1) for _ in range(N1 + 1)]

        def minDist(index1, index2):
            if index1 == N1:
                return N2 - index2
            if index2 == N2:
                return N1 - index1
            if has_cache[index1][index2]:
                return cache[index1][index2]

            best = INF
            if word1[index1] == word2[index2]:
                best = min(best, minDist(index1 + 1, index2 +1))
            best = min(best, minDist(index1, index2 + 1) + 1)
            best = min(best, minDist(index1 + 1, index2) +1)
            best = min(best, minDist(index1+1, index2 +1) +1)

            has_cache[index1][index2] = True
            cache[index1][index2] = best
            return best
        return minDist(0,0)
