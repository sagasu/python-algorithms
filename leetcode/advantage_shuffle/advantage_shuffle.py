class Solution:
    def advantageCount(self, A: List[int], B: List[int]) -> List[int]:
        N = len(A)
        B = sorted(list((x, index) for index, x in enumerate(B)), reverse=True)
        A.sort(reverse=True)

        ans = [-1] * N
        unused = []
        bpointer = 0
        for x in A:
            while bpointer < len(B) and x <= B[bpointer][0]:
                bpointer += 1
            if bpointer < len(B):
                ans[B[bpointer][1]] = x
                bpointer += 1
            else:
                unused.append(x)

        for apointer in range(N):
            if ans[apointer] == -1:
                ans[apointer] = unused.pop()

        return ans

