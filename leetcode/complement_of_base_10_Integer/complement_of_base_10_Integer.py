class Solution:
    def bitwiseComplement(self, N: int) -> int:
        s = str(bin(N))[2:]
        n = ''
        for c in s:
            if c == '1':
                n += '0'
            else:
                n += '1'
        return int(n,2)