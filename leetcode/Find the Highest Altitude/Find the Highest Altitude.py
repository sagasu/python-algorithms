class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        max_alt = 0
        curr = 0
        for g in gain:
            curr += g
            if curr > max_alt:
                max_alt = curr
        return max_alt