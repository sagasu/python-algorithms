from typing import List


class Solution:
    def minimizeSum(self, nums: List[int]) -> int:
        """Sort and minimize the remaining range after changing two extremes (low score can always be 0)."""
        nums.sort()
        return min(nums[-1] - nums[2], nums[-3] - nums[0], nums[-2] - nums[1])


if __name__ == "__main__":
    sol = Solution()
    tests = [
        ([1, 4, 7, 8, 5], 3),
        ([1, 4, 3], 0),
    ]
    failed = False
    for nums, expected in tests:
        got = sol.minimizeSum(nums)
        if got == expected:
            print("OK")
        else:
            print("FAIL")
            failed = True
    if failed:
        raise SystemExit(1)
