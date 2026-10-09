class Solution:
    def minInsertions(self, s: str) -> int:
        """
        '(' is closed only by two consecutive ')'.

        `need` is how many ')' are still required. A '(' adds 2, after closing
        an odd leftover ')' with one insertion so pairs stay aligned. A ')'
        spends one required character; if none is required, insert a '(' and
        count this ')' as the first of the two it needs.
        """
        insertions = 0
        need = 0
        for ch in s:
            if ch == "(":
                if need % 2:
                    insertions += 1
                    need -= 1
                need += 2
            else:
                need -= 1
                if need < 0:
                    insertions += 1
                    need = 1
        return insertions + need


if __name__ == "__main__":
    sol = Solution()
    tests = [
        ("(()))", 1),
        ("())", 0),
        ("))())(", 3),
        (")", 2),
        ("(((", 6),
        (")(", 4),
        ("())(())))", 0),
        ("(())())))", 0),
    ]
    failed = False
    for s, expected in tests:
        got = sol.minInsertions(s)
        status = "OK" if got == expected else "FAIL"
        if got != expected:
            failed = True
        print(f"{status}: s={s!r} -> {got} (expected {expected})")
    if failed:
        raise SystemExit(1)
