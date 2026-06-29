class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        count = 0
        N = len(A)

        delta = float("inf")
        lenght = 2

        for index in range(N-1):
            x, y = A[index], A[index + 1]

            if y - x == delta:
                length += 1
            else:
                delta = y - x
                length = 2

            count += max(length - 2, 0)

        return count