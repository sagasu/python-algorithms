from typing import List


class Solution:
    def sortPermutation(self, nums: List[int]) -> int:
        """Max k is the AND of all misplaced values (star through k sorts them); 0 if already sorted."""
        k = -1
        for i, x in enumerate(nums):
            if x != i:
                k &= x
        return 0 if k == -1 else k


if __name__ == "__main__":
    sol = Solution()
    tests = [
        ([0, 3, 2, 1], 1),
        ([0, 1, 3, 2], 2),
        ([3, 2, 1, 0], 0),
    ]
    failed = False
    for nums, expected in tests:
        got = sol.sortPermutation(nums)
        if got == expected:
            print("OK")
        else:
            print("FAIL")
            failed = True
    if failed:
        raise SystemExit(1)
