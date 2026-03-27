from typing import List


class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        n = len(mat[0])
        shift = k % n  # effective shift after full cycles cancel out

        if shift == 0:
            return True  # every row is back to original

        for i, row in enumerate(mat):
            if i % 2 == 0:
                # even rows shift left by `shift`: row[j] should equal row[(j + shift) % n]
                if any(row[j] != row[(j + shift) % n] for j in range(n)):
                    return False
            else:
                # odd rows shift right by `shift`: row[j] should equal row[(j - shift) % n]
                if any(row[j] != row[(j - shift) % n] for j in range(n)):
                    return False

        return True
