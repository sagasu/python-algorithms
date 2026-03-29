class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        # Swaps are only between indices 2 apart, so even-indexed chars
        # can only rearrange among themselves, same for odd-indexed chars.
        return sorted(s1[::2]) == sorted(s2[::2]) and sorted(s1[1::2]) == sorted(s2[1::2])
