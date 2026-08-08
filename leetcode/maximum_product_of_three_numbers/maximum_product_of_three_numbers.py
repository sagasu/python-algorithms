from typing import List


class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        """
        628. Maximum Product of Three Numbers

        After sorting, the max product of three numbers is the larger of:
          1) three largest values (all positive, or least-negative if all negative)
          2) two smallest (most negative) * largest (neg*neg*pos can dominate)

        Time:  O(n log n)
        Space: O(1) extra if sort is in-place (O(n) depending on sort impl)
        """
        nums.sort()
        return max(
            nums[-1] * nums[-2] * nums[-3],
            nums[0] * nums[1] * nums[-1],
        )


if __name__ == "__main__":
    s = Solution()
    assert s.maximumProduct([1, 2, 3]) == 6
    assert s.maximumProduct([1, 2, 3, 4]) == 24
    assert s.maximumProduct([-1, -2, -3]) == -6
    assert s.maximumProduct([-4, -3, -2, -1, 60]) == 720
    assert s.maximumProduct([-100, -98, -1, 2, 3, 4]) == 39200
    assert s.maximumProduct([-1, -2, 1, 2, 3]) == 6
    assert s.maximumProduct([0, 0, 0]) == 0
    assert s.maximumProduct([-5, 0, 1, 2]) == 0
    print("ok")
