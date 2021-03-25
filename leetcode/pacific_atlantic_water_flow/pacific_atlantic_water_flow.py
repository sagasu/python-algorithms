class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix: return []
        M,N = len(matrix), len(matrix[0])
        p,a=[],[]
        vp,va = set(), set()

        for r in range(M):
            p.append((r,0))
            a.append((r,N-1))
        for c in range(N):
            p.append((0,c))
            a.append((M-1,c))
        dirs = [(1,0),(-1,0),(0,1),(0,-1)]
        def dfs(r,c,visited):
            visited.add((r,c))
            for di,dj in dirs:
                new_r, new_c = r+di,c+dj
                if 0<=new_r<M and 0<=new_c<N and matrix[r][c]<=matrix[new_r][new_c] and (new_r,new_c) not in visited:
                    dfs(new_r,new_c,visited)

        for r,c in p: dfs(r,c,vp)
        for r,c in a: dfs(r,c,va)

        return vp & va