from typing import List


class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        """Sum squares of 1-indexed elements whose index divides n."""
        n = len(nums)
        return sum(nums[i - 1] ** 2 for i in range(1, n + 1) if n % i == 0)


if __name__ == "__main__":
    sol = Solution()
    tests = [
        ([1, 2, 3, 4], 21),
        ([2, 7, 1, 19, 18, 3], 63),
    ]
    failed = False
    for nums, expected in tests:
        got = sol.sumOfSquares(nums)
        status = "OK" if got == expected else "FAIL"
        if got != expected:
            failed = True
        print(f"{status}: nums={nums} -> {got} (expected {expected})")
    if failed:
        raise SystemExit(1)
