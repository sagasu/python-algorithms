class Solution:
    def sumAndMultiply(self, n: int) -> int:
        x = s = 0
        p = 1
        while n:
            n, d = divmod(n, 10)
            if d:
                x += p * d
                s += d
                p *= 10
        return x * s