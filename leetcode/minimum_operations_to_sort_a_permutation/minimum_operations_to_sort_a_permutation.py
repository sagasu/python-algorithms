from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        """Dihedral orbit: only circular ±1 sequences are sortable; min of left-rotates vs reverse+rotates."""
        n = len(nums)
        if n <= 1:
            return 0

        def is_step(step: int) -> bool:
            for i in range(n):
                if (nums[i] + step) % n != nums[(i + 1) % n]:
                    return False
            return True

        start = nums[0]
        if is_step(1):
            return 0 if start == 0 else min(n - start, start + 2)
        if is_step(n - 1):
            return min(n - start, start + 2)
        return -1


if __name__ == "__main__":
    sol = Solution()
    tests = [
        ([0, 2, 1], 2),
        ([1, 0, 2], 2),
        ([2, 0, 1, 3], -1),
    ]
    failed = False
    for nums, expected in tests:
        got = sol.minOperations(nums)
        if got == expected:
            print("OK")
        else:
            print("FAIL")
            failed = True
    if failed:
        raise SystemExit(1)
