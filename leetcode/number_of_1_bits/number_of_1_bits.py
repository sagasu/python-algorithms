class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0

        for _ in range(32):
            count += n % 2
            n //= 2

        return count