class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = []

        def string_representation(board):
            s = []
            for col in board:
                s.append("." * (col) + "Q" + "." * (n - col - 1))
            return s
        
        def solve(row, previous):
            if row == n:
                ans.append(string_representation(previous))
                return
            for col in range(n):
                solve(row + 1, previous + [col])
        solve(0, [])
        return ans