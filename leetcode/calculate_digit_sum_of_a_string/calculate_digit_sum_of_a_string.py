class Solution:
    def digitSum(self, s: str, k: int) -> str:
        """Simulate rounds: replace each k-sized group with its digit sum until len(s) <= k."""
        while len(s) > k:
            parts = []
            for i in range(0, len(s), k):
                group = s[i : i + k]
                parts.append(str(sum(int(c) for c in group)))
            s = "".join(parts)
        return s


if __name__ == "__main__":
    sol = Solution()
    tests = [
        ("11111222223", 3, "135"),
        ("00000000", 3, "000"),
    ]
    failed = False
    for s, k, expected in tests:
        got = sol.digitSum(s, k)
        if got == expected:
            print("OK")
        else:
            print("FAIL")
            failed = True
    if failed:
        raise SystemExit(1)
