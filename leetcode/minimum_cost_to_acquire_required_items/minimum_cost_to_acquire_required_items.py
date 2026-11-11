class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        """Cost in the combo count is piecewise linear; min is at 0, min(need), or max(need)."""

        def cost(both: int) -> int:
            return (
                both * costBoth
                + max(0, need1 - both) * cost1
                + max(0, need2 - both) * cost2
            )

        return min(cost(0), cost(min(need1, need2)), cost(max(need1, need2)))


if __name__ == "__main__":
    sol = Solution()
    tests = [
        (3, 2, 1, 3, 2, 3),
        (5, 4, 15, 2, 3, 22),
        (5, 4, 15, 0, 0, 0),
    ]
    failed = False
    for cost1, cost2, costBoth, need1, need2, expected in tests:
        got = sol.minimumCost(cost1, cost2, costBoth, need1, need2)
        if got == expected:
            print("OK")
        else:
            print("FAIL")
            failed = True
    if failed:
        raise SystemExit(1)
