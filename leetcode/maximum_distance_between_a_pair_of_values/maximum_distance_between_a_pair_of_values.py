from typing import List


class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        ans = 0
        for i, v in enumerate(nums1):
            if i >= len(nums2):
                break  # j must be >= i, but j < len(nums2), so no valid j exists
            # Find rightmost j >= i where nums2[j] >= v (nums1[i] <= nums2[j])
            # nums2 is non-increasing, so nums2[j] >= v holds for j in [i, threshold]
            lo, hi = i, len(nums2) - 1
            while lo < hi:
                mid = (lo + hi + 1) // 2
                if nums2[mid] >= v:
                    lo = mid
                else:
                    hi = mid - 1
            if nums2[lo] >= v:
                ans = max(ans, lo - i)
        return ans
