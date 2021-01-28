class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        result = ""

        for index in range(n):
            digitsLeft = n - index - 1

            for c in range(1, 27):
                if k - c <= digitsLeft * 26:
                    k -= c
                    result += chr(ord('a') + c -1)
                    break
        return result