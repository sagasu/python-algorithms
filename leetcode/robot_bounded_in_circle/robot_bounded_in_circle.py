class Solution:
    def isRobotBounded(self, i):
        s, d = 90, [0, 0]
        for a in i: 
            if a == 'L': s = (s + 90) % 360
            elif a == 'R': s = (s - 90) % 360
            else:
                if s == 90: d[1] += 1
                elif s == 180: d[0] -= 1
                elif s == 270: d[1] -= 1
                else: d[0] += 1
        return s != 90 or d == [0, 0]