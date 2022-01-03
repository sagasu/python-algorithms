class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        l = [0 for i in range(0,N)]
        
        for t in trust:
            l[t[1]-1]+=1
            l[t[0]-1]-=1
        for s in range(0,N):
            if l[s] == N-1 :
                return s+1
        return -1