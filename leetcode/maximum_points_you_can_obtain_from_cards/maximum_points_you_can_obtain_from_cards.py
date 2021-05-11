class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        N = len(cardPoints)
        best = 0

        front = sum(cardPoints[:k])
        back = 0

        best = max(best, front + back)

        for offset in range(k):
            front -= cardPoints[k - offset - 1]
            back += cardPoints[N - offset -1]
            best = max(best, front + back)
        return best