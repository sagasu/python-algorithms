from typing import List


class Solution:
    def minMoves(self, nums: List[int]) -> int:
        """Only increments are allowed, so raise every value to the current max."""
        target = max(nums)
        return sum(target - x for x in nums)


if __name__ == "__main__":
    s = Solution()
    tests = [
        ([2, 1, 3], 3),
        ([4, 4, 5], 2),
    ]
    failed = False
    for nums, expected in tests:
        got = s.minMoves(nums)
        if got == expected:
            print("OK")
        else:
            print("FAIL")
            failed = True
    if failed:
        raise SystemExit(1)
