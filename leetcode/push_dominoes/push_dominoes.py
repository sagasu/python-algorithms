class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        N = len(dominoes)
        inf = 10 ** 10
        right = [inf] * N
        left = [inf] * N
        
        cur = inf
        for index in range(N):
            if dominoes[index] == 'R':
                cur = 0
            elif dominoes[index] == 'L':
                cur = inf
            else:
                cur +=1
            cur = min(cur, inf)
            right[index] = cur
        cur = inf
        for index in range(N):
            if dominoes[N-index-1] == 'L':
                cur = 0
            elif dominoes[N-index-1] == 'R':
                cur = inf
            else:
                cur += 1
            cur = min(cur, inf)
            left[N - index -1] = cur
        ans = []
        for index in range(N):
            if right[index]<left[index]:
                ans.append("R")
            elif right[index] > left[index]:
                ans.append("L")
            else:
                ans.append(".")
        return "".join(ans)
