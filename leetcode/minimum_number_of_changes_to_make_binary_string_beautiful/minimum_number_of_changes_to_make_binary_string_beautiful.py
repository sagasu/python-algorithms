class Solution:
    def minChanges(self, s: str) -> int:
        """Count mismatched adjacent pairs; each even-length block is those pairs of 00/11."""
        return sum(s[i] != s[i + 1] for i in range(0, len(s), 2))


if __name__ == "__main__":
    sol = Solution()
    tests = [
        ("1001", 2),
        ("10", 1),
        ("0000", 0),
    ]
    failed = False
    for s, expected in tests:
        got = sol.minChanges(s)
        if got == expected:
            print("OK")
        else:
            print("FAIL")
            failed = True
    if failed:
        raise SystemExit(1)
