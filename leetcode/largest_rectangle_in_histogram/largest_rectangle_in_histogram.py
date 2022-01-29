class Solution:
    def largestRectangleArea(self, A):
        ans = 0
        
        A.extend([0])
        
        mono = [(0, -1)]
        for i, e in enumerate(A):
            if e > mono[-1][0]:
                mono.append((e, i))
            elif e < mono[-1][0]:
                j = None
                while mono and e < mono[-1][0]:
                    higher, j = mono.pop()
                    ans = max(ans, higher*(i-j))
                mono.append((e, j))
        
        return ans