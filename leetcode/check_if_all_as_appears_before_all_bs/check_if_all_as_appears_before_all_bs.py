class Solution:
    def checkString(self, s: str) -> bool:
        """True iff no 'a' appears after a 'b' (equivalently, 'ba' is absent)."""
        return "ba" not in s


if __name__ == "__main__":
    sol = Solution()
    tests = [
        ("aaabbb", True),
        ("abab", False),
        ("bbb", True),
    ]
    failed = False
    for s, expected in tests:
        got = sol.checkString(s)
        if got == expected:
            print("OK")
        else:
            print("FAIL")
            failed = True
    if failed:
        raise SystemExit(1)
