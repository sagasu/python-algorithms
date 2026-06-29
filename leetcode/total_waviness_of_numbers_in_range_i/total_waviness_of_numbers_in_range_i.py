class Solution:
    def totalWaviness(self, l: int, r: int) -> int:
        def waviness(n: int) -> int:
            digits = [int(d) for d in str(n)]
            if len(digits) < 3:
                return 0
            count = 0
            for i in range(1, len(digits) - 1):
                if digits[i] > digits[i-1] and digits[i] > digits[i+1]:  # peak
                    count += 1
                elif digits[i] < digits[i-1] and digits[i] < digits[i+1]:  # valley
                    count += 1
            return count

        return sum(waviness(n) for n in range(l, r + 1))
