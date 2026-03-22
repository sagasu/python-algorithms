from typing import List


class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        def rotate90(m: List[List[int]]) -> List[List[int]]:
            # Rotate 90° clockwise: transpose then reverse each row
            n = len(m)
            return [[m[n - 1 - j][i] for j in range(n)] for i in range(n)]

        for _ in range(4):
            if mat == target:
                return True
            mat = rotate90(mat)
        return False
