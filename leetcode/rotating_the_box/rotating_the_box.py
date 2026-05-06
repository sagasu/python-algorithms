from typing import List


class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        m, n = len(box), len(box[0])

        # Step 1: apply gravity — stones fall to the right in each row
        for row in box:
            empty = n - 1  # next available slot from the right
            for j in range(n - 1, -1, -1):
                if row[j] == '*':
                    empty = j - 1  # obstacle resets the empty pointer
                elif row[j] == '#':
                    row[j], row[empty] = row[empty], row[j]
                    empty -= 1

        # Step 2: rotate 90° clockwise
        # New grid is n x m: result[j][m-1-i] = box[i][j]
        result = [[''] * m for _ in range(n)]
        for i in range(m):
            for j in range(n):
                result[j][m - 1 - i] = box[i][j]

        return result
