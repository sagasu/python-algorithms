from typing import List


class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        """
        Squares erase sign, so only magnitudes matter. Even indices add a square
        and odd indices subtract one, and there are ceil(n/2) even slots.
        Sort squares ascending and subtract the smallest floor(n/2) of them.
        """
        squares = sorted(x * x for x in nums)
        neg = len(squares) // 2
        return sum(squares[neg:]) - sum(squares[:neg])


if __name__ == "__main__":
    sol = Solution()
    tests = [
        ([1, 2, 3], 12),
        ([1, -1, 2, -2, 3, -3], 16),
    ]
    failed = False
    for nums, expected in tests:
        got = sol.maxAlternatingSum(nums)
        status = "OK" if got == expected else "FAIL"
        if got != expected:
            failed = True
        print(f"{status}: nums={nums} -> {got} (expected {expected})")
    if failed:
        raise SystemExit(1)
