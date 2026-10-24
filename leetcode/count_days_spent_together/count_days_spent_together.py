class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        """Convert MM-DD to day-of-year, then take inclusive interval overlap length."""
        days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        def to_day(date: str) -> int:
            month, day = int(date[:2]), int(date[3:])
            return sum(days_in_month[: month - 1]) + day

        start = max(to_day(arriveAlice), to_day(arriveBob))
        end = min(to_day(leaveAlice), to_day(leaveBob))
        return max(0, end - start + 1)


if __name__ == "__main__":
    sol = Solution()
    tests = [
        ("08-15", "08-18", "08-16", "08-19", 3),
        ("10-01", "10-31", "11-01", "12-31", 0),
    ]
    failed = False
    for arriveAlice, leaveAlice, arriveBob, leaveBob, expected in tests:
        got = sol.countDaysTogether(arriveAlice, leaveAlice, arriveBob, leaveBob)
        if got == expected:
            print("OK")
        else:
            print("FAIL")
            failed = True
    if failed:
        raise SystemExit(1)
