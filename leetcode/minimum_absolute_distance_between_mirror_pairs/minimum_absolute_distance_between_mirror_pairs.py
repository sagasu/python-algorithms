from typing import List


class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        def reverse(x: int) -> int:
            y = 0
            while x:
                y = y * 10 + x % 10
                x //= 10
            return y

        pos = {}  # reversed value -> last index seen
        ans = float('inf')

        for i, x in enumerate(nums):
            # If x was stored as a reverse of some earlier number, it's a mirror pair
            if x in pos:
                ans = min(ans, i - pos[x])
            # Store reverse(x) so future numbers equal to reverse(x) can find this index
            pos[reverse(x)] = i

        return -1 if ans == float('inf') else ans
