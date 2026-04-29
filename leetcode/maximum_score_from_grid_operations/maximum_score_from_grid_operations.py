from typing import List


class Solution:
    def maximumScore(self, grid: List[List[int]]) -> int:
        n = len(grid)

        # prefix[j][i] = sum of first i elements in column j
        prefix = [[0] * (n + 1) for _ in range(n)]
        for j in range(n):
            for i in range(n):
                prefix[j][i + 1] = prefix[j][i] + grid[i][j]

        # prevPick[i] = max score up to prev column, where prev column has
        #               its bottom selected row at index i-1 (i rows selected)
        # prevSkip[i] = same but prev column was "skipped" (not the one we
        #               just colored) — the last colored column had i rows
        prevPick = [0] * (n + 1)
        prevSkip = [0] * (n + 1)

        for j in range(1, n):
            currPick = [0] * (n + 1)
            currSkip = [0] * (n + 1)

            for curr in range(n + 1):   # rows selected in current column j
                for prev in range(n + 1):  # rows selected in previous column j-1
                    if curr > prev:
                        # Current column extends deeper than previous.
                        # Rows prev..curr-1 in column j-1 are black while j is also black
                        # → score comes from col j-1 rows [prev, curr)
                        score = prefix[j - 1][curr] - prefix[j - 1][prev]
                        currPick[curr] = max(currPick[curr], prevSkip[prev] + score)
                        currSkip[curr] = max(currSkip[curr], prevSkip[prev] + score)
                    else:
                        # Previous column extends deeper than current.
                        # Rows curr..prev-1 in column j are black while j-1 is also black
                        # → score comes from col j rows [curr, prev)
                        score = prefix[j][prev] - prefix[j][curr]
                        currPick[curr] = max(currPick[curr], prevPick[prev] + score)
                        currSkip[curr] = max(currSkip[curr], prevPick[prev])

            prevPick = currPick
            prevSkip = currSkip

        return max(prevPick)
