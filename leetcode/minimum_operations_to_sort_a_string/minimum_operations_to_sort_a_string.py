class Solution:
    def minOperations(self, s: str) -> int:
        """Proper substring sorts: 0 if sorted, 1 if an end already matches min/max, 2 if min or max can move in one end-sort, else 3 (or -1 when n==2)."""
        n = len(s)
        if all(s[i] <= s[i + 1] for i in range(n - 1)):
            return 0
        if n == 2:
            return -1
        mn, mx = min(s), max(s)
        if s[0] == mn or s[-1] == mx:
            return 1
        if mn in s[:-1] or mx in s[1:]:
            return 2
        return 3


if __name__ == "__main__":
    sol = Solution()
    tests = [
        ("dog", 1),
        ("card", 2),
        ("gf", -1),
    ]
    failed = False
    for s, expected in tests:
        got = sol.minOperations(s)
        if got == expected:
            print("OK")
        else:
            print("FAIL")
            failed = True
    if failed:
        raise SystemExit(1)
