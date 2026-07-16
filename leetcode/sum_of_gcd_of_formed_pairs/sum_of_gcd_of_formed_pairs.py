from math import gcd
from typing import List


class Solution:
    def gcdSum(self, nums: List[int]) -> int:
        """
        3867. Sum of GCD of Formed Pairs

        1. prefixGcd[i] = gcd(nums[i], max(nums[0..i]))
           - If nums[i] is a new prefix max, this equals nums[i].
           - Otherwise it is gcd of the value and the running max.
        2. Sort prefixGcd ascending.
        3. Pair ends: (smallest, largest), (next smallest, next largest), ...
           Odd-length middle element is left unpaired.
        4. Return sum of gcd of each pair.

        Time:  O(n log n + n log M)  (sort + gcd)
        Space: O(n)
        """
        n = len(nums)
        prefix_gcd = [0] * n
        mx = 0
        for i, x in enumerate(nums):
            mx = max(mx, x)
            prefix_gcd[i] = gcd(x, mx)

        prefix_gcd.sort()
        return sum(
            gcd(prefix_gcd[i], prefix_gcd[n - 1 - i]) for i in range(n // 2)
        )


if __name__ == "__main__":
    s = Solution()
    assert s.gcdSum([2, 6, 4]) == 2
    assert s.gcdSum([3, 6, 2, 8]) == 5
    assert s.gcdSum([1]) == 0  # single element: no pairs
    assert s.gcdSum([5, 5]) == 5  # prefixGcd=[5,5], gcd(5,5)=5
    assert s.gcdSum([7, 1, 1, 1]) == 2  # prefix: [7,1,1,1] -> sort [1,1,1,7]
    # pairs: gcd(1,7)+gcd(1,1)=1+1=2
    print("ok")
