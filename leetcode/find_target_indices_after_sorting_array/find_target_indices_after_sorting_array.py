from __future__ import annotations


class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        """Count values < target (start index) and == target (run length)."""
        less = equal = 0
        for x in nums:
            if x < target:
                less += 1
            elif x == target:
                equal += 1
        return list(range(less, less + equal))


if __name__ == "__main__":
    sol = Solution()
    tests = [
        ([1, 2, 5, 2, 3], 2, [1, 2]),
        ([1, 2, 5, 2, 3], 3, [3]),
        ([1, 2, 5, 2, 3], 5, [4]),
    ]
    failed = False
    for nums, target, expected in tests:
        got = sol.targetIndices(nums, target)
        status = "OK" if got == expected else "FAIL"
        if got != expected:
            failed = True
        print(f"{status}: nums={nums} target={target} -> {got} (expected {expected})")
    if failed:
        raise SystemExit(1)
