class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        filled = [[0.0] * (query_row + 2) for _ in range (query_row+2)]
        filled[0][0] = poured

        for row in range(query_row + 1):
            for col in range(query_row + 1):
                if (filled[row][col] > 1.0):
                    overfill = filled[row][col] - 1.0

                    filled[row + 1][col]    += overfill / 2.0
                    filled[row + 1][col +1] += overfill /2.0

        # if needs to be here because we are not removing overfill from glasses that are overflowing, the maximum they can hold is 1
        return filled[query_row][query_glass] if filled[query_row][query_glass] <= 1 else 1