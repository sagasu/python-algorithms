class Solution:
    def addBinary(self, a: str, b: str) -> str:
        rt = int(a, 2) + int(b, 2)
        return bin(rt)[2:]