class Solution:
    def findComplement(self, num: int) -> int:
        return int(''.join(['1' if c == '0' else '0' for c in str(bin(num))[2:]]),2)