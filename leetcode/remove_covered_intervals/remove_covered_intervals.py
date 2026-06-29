class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()            
        trap, count = intervals[0], 0                     
        for i in intervals[1:]:                 
            if i[0] == trap[0] or i[1] <= trap[1]:       
                count += 1
                trap[1] = max(trap[1], i[1])       
            else:  trap = i
        return len(intervals) -  count