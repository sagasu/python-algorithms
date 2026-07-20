from typing import List


class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        """
        1260. Shift 2D Grid

        Treat the m x n grid as a flattened 1D array of length m*n.
        One shift is a right-rotate by 1 in that array (last -> first).
        After k shifts, element at flat index i moves to (i + k) % (m*n).

        Time:  O(m * n)
        Space: O(m * n) for the result
        """
        m, n = len(grid), len(grid[0])
        total = m * n
        k %= total
        ans = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                ni, nj = divmod((i * n + j + k) % total, n)
                ans[ni][nj] = grid[i][j]
        return ans


if __name__ == "__main__":
    s = Solution()
    assert s.shiftGrid([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 1) == [
        [9, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
    ]
    assert s.shiftGrid([[3, 8, 1, 9], [19, 7, 2, 5], [4, 6, 11, 10], [12, 0, 21, 13]], 4) == [
        [12, 0, 21, 13],
        [3, 8, 1, 9],
        [19, 7, 2, 5],
        [4, 6, 11, 10],
    ]
    assert s.shiftGrid([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 9) == [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ]
    assert s.shiftGrid([[1], [2], [3], [4], [5], [6], [7]], 23) == [
        [6],
        [7],
        [1],
        [2],
        [3],
        [4],
        [5],
    ]
    print("ok")
