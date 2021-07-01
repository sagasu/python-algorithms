class Solution:
    def grayCode(self, n: int) -> List[int]:
        used = set()
        used.add(0)
        ans = [0]

        for _ in range(1 << n):
            for x in range(n):
                if((1 << x) ^ ans[-1]) not in used:
                    nxt = (1 << x) ^ ans[-1]
                    used.add(nxt)
                    ans.append(nxt)
                    break
        return ans