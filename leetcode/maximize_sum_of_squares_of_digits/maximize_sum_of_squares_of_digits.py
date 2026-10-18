class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        """Greedy: as many 9s as possible (max sum of squares), then remainder, then zeros (largest number)."""
        if sum > 9 * num:
            return ""
        nines, rem = divmod(sum, 9)
        zeros = num - nines - (1 if rem else 0)
        parts = []
        if nines:
            parts.append("9" * nines)
        if rem:
            parts.append(str(rem))
        if zeros:
            parts.append("0" * zeros)
        return "".join(parts)


if __name__ == "__main__":
    s = Solution()
    tests = [
        (2, 3, "30"),
        (2, 17, "98"),
        (1, 10, ""),
    ]
    failed = False
    for num, digit_sum, expected in tests:
        got = s.maxSumOfSquares(num, digit_sum)
        if got == expected:
            print("OK")
        else:
            print("FAIL")
            failed = True
    if failed:
        raise SystemExit(1)
