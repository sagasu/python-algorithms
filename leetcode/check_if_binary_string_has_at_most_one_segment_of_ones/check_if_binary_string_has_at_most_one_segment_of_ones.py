class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        # The string starts with '1' (guaranteed by constraints).
        # If "01" exists, a 0 appeared after some 1s and then 1s resumed -> 2+ segments.
        return "01" not in s
