class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        
        if not points:
            return 0
        
        ps = sorted(points, key=lambda e: e[1])
        p0 = ps[0][1]
        res = 1
        for i in range(1, len(ps)):
            if ps[i][0] > p0:
                p0 = ps[i][1]
                res += 1
        return res