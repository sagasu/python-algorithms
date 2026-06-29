class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        cols = len(encodedText) // rows

        # Read diagonals: each diagonal k starts at row 0, col k
        # and steps down-right: (r, k+r) for r in 0..rows-1
        result = []
        for k in range(cols):
            for r in range(rows):
                col = k + r
                if col >= cols:
                    break
                result.append(encodedText[r * cols + col])

        return ''.join(result).rstrip(' ')
