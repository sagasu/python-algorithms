class Solution:
        
    def cherryPickup(self, grid: List[List[int]]) -> int:
        
        if not grid or not grid[0]:
            return 0
        
        m,n = len(grid),len(grid[0])
        
        dp = {}
        for i in range(m):
            for j1 in range(n):
                for j2 in range(j1,n):
                    if i == 0:
                        if (j1,j2) == (0,n-1):        
                            dp[(i,j1,j2)] = grid[0][j1] + grid[0][j2]*(j1 != j2)
                        continue
                    prev = -1
                    for t1 in range(j1-1,j1+2):
                        for t2 in range(j2-1,j2+2):
                            if (i-1,t1,t2) in dp:
                                prev = max(dp[(i-1,t1,t2)], prev)
                    if prev != -1:
                        dp[(i,j1,j2)] = grid[i][j1] + grid[i][j2]*(j1 != j2) + prev
        
        ans = 0
        for j1 in range(m):
            for j2 in range(j1,n):
                if (m-1,j1,j2) in dp:
                    ans = max(ans,dp[(m-1,j1,j2)])
        
        return ans