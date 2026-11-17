class Solution:
    # Min semi-palindrome cost for every substring, then DP into k parts of length >= 2.
    def minimumChanges(self, s: str, k: int) -> int:
        n = len(s)
        inf = n + 1
        divisors = [[] for _ in range(n + 1)]
        for d in range(1, n):
            for length in range(d * 2, n + 1, d):
                divisors[length].append(d)

        cost = [[inf] * (n + 1) for _ in range(n)]
        for i in range(n):
            for j in range(i + 2, n + 1):
                length = j - i
                best = inf
                for d in divisors[length]:
                    changes = 0
                    group_len = length // d
                    for r in range(d):
                        left, right = 0, group_len - 1
                        while left < right:
                            if s[i + r + left * d] != s[i + r + right * d]:
                                changes += 1
                            left += 1
                            right -= 1
                    if changes < best:
                        best = changes
                cost[i][j] = best

        dp = [inf] * (n + 1)
        dp[0] = 0
        for _ in range(k):
            ndp = [inf] * (n + 1)
            for i in range(n):
                if dp[i] == inf:
                    continue
                base = dp[i]
                for j in range(i + 2, n + 1):
                    val = base + cost[i][j]
                    if val < ndp[j]:
                        ndp[j] = val
            dp = ndp
        return dp[n]


if __name__ == "__main__":
    sol = Solution()
    tests = [
        ("abcac", 2, 1),
        ("abcdef", 2, 2),
        ("aabbaa", 3, 0),
    ]
    failed = False
    for s, k, expected in tests:
        got = sol.minimumChanges(s, k)
        if got == expected:
            print("OK")
        else:
            print("FAIL")
            failed = True
    if failed:
        raise SystemExit(1)
