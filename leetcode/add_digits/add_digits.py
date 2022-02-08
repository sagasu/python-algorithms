class Solution:
    def addDigits(self, num: int) -> int:
        return 9 if num % 9 == 0 and num > 0 else num % 9