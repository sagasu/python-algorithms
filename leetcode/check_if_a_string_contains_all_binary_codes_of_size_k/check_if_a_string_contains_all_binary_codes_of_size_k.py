class Solution:

    # Time O(1)
    def hasAllCodes(self, s: str, k: int) -> bool:
        N = len(s)
        M = 2 ** k

        if M > N:
            return False

        seen = [False] * M

        current = 0
        for index in range(N):
            current *= 2
            current += int(s[index])
            current %= M

            if index >= k - 1:
                seen[current] = True
                
        return all(seen) 