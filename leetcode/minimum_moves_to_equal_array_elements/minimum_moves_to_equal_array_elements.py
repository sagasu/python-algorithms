from __future__ import annotations


class Solution:
    def minMoves(self, nums: list[int]) -> int:
        """Incrementing n - 1 elements equals decrementing one. Moves are the gaps to the minimum."""
        low = min(nums)
        return sum(x - low for x in nums)


if __name__ == "__main__":
    sol = Solution()
    tests = [
        ([1, 2, 3], 3),
        ([1, 1, 1], 0),
    ]
    failed = False
    for nums, expected in tests:
        got = sol.minMoves(nums)
        status = "OK" if got == expected else "FAIL"
        if got != expected:
            failed = True
        print(f"{status}: nums={nums} -> {got} (expected {expected})")
    if failed:
        raise SystemExit(1)
