class Solution:
    def canAliceWin(self, n: int) -> bool:
        """Simulate turns that remove 10 stones, then 9, then 8, and so on."""
        remove = 10
        alice_turn = True
        while remove > 0 and n >= remove:
            n -= remove
            remove -= 1
            alice_turn = not alice_turn
        return not alice_turn


if __name__ == "__main__":
    sol = Solution()
    tests = [
        (12, True),
        (1, False),
    ]
    failed = False
    for n, expected in tests:
        got = sol.canAliceWin(n)
        if got == expected:
            print("OK")
        else:
            print("FAIL")
            failed = True
    if failed:
        raise SystemExit(1)
