class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        # Swaps allowed between indices with even difference -> same parity indices
        # can be freely rearranged among themselves.
        return sorted(s1[::2]) == sorted(s2[::2]) and sorted(s1[1::2]) == sorted(s2[1::2])
