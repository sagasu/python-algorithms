class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)
        if s[-1] != '0':
            return False

        # reach[i] = 1 if index i is reachable, else 0
        reach = [0] * n
        reach[0] = 1

        # prefix[i] = sum of reach[0..i-1]
        prefix = [0] * (n + 1)
        prefix[1] = 1

        for i in range(1, n):
            if s[i] == '0':
                # Check if any reachable index in [i-maxJump, i-minJump] exists
                lo = max(0, i - maxJump)
                hi = i - minJump
                if hi >= 0 and prefix[hi + 1] - prefix[lo] > 0:
                    reach[i] = 1
            prefix[i + 1] = prefix[i] + reach[i]

        return reach[n - 1] == 1
