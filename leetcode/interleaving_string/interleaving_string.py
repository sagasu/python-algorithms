class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        N1 = len(s1)
        N2 = len(s2)
        N3 = len(s3)
        if N1 + N2 != N3:
            return False

        cache = [[False] * (N2 +1) for _ in range(N1 + 1)]
        has_cache = [[False] * (N2+1) for _ in range(N1 +1)]

        def canInterleave(index1, index2):
            if has_cache[index1][index2]:
                return cache[index1][index2]

            index3 = index1 + index2

            if index3 == N3:
                has_cache[index1][index2] = cache[index1][index2] = True
                return True

            if index1 < N1 and s1[index1] == s3[index3] and canInterleave(index1 +1, index2):
                has_cache[index1][index2] = cache[index1][index2] = True
                return True
            if index2 < N2 and s2[index2] == s3[index3] and canInterleave(index1, index2 +1):
                has_cache[index1][index2] = cache[index1][index2] = True
                return True
                
            has_cache[index1][index2] = True
            cache[index1][index2] = False    
            return False
        return canInterleave(0,0)