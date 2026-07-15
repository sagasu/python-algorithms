from math import gcd


class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        """
        sumOdd  = 1+3+...+(2n-1) = n^2
        sumEven = 2+4+...+2n     = n(n+1)
        gcd(n^2, n(n+1)) = n * gcd(n, n+1) = n  (n and n+1 coprime)
        """
        return n

    def gcdOfOddEvenSums_explicit(self, n: int) -> int:
        """Same result via formulas + gcd (for clarity / verification)."""
        sum_odd = n * n
        sum_even = n * (n + 1)
        return gcd(sum_odd, sum_even)


if __name__ == "__main__":
    s = Solution()
    assert s.gcdOfOddEvenSums(4) == 4
    assert s.gcdOfOddEvenSums(5) == 5
    assert s.gcdOfOddEvenSums(1) == 1
    for n in range(1, 101):
        assert s.gcdOfOddEvenSums(n) == s.gcdOfOddEvenSums_explicit(n) == n
    print("ok")
