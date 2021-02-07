class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        N = len(s)
        ans = [N] * N

        current = N
        for index, x in enumerate(s):
            if x ==c:
                current = 0
            else:
                current += 1

            ans[index] = min(ans[index], current)

        index = N -1
        current = N
        while index >= 0:
            if s[index] == c:
                current = 0
            else:
                current += 1

            ans[index] = min(ans[index], current)
            index -= 1

        return ans