class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        return max(abs(sx - fx), abs(sy - fy)) <= t if max(abs(sx - fx), abs(sy - fy)) != 0 else t != 1       