from typing import List


class Solution:
    def minMoves(self, nums: List[int], limit: int) -> int:
        n = len(nums)
        # diff[t] = change in moves when target sum goes from t-1 to t
        # Range of t: [2, 2*limit]
        size = 2 * limit + 2
        diff = [0] * (size + 1)

        for i in range(n // 2):
            a, b = nums[i], nums[n - 1 - i]
            lo, hi = min(a, b), max(a, b)
            s = a + b

            # Default: 2 moves for all t
            # [2, lo]: 2 moves → no change needed (already 2)
            # [lo+1, s-1]: 1 move → subtract 1 at lo+1
            # [s, s]: 0 moves → subtract 1 more at s
            # [s+1, hi+limit]: 1 move → add 1 back at s+1
            # [hi+limit+1, 2*limit]: 2 moves → add 1 more at hi+limit+1

            diff[2] += 2
            diff[size] -= 2          # end sentinel

            diff[lo + 1] -= 1        # drop to 1 move
            diff[s] -= 1             # drop to 0 moves
            diff[s + 1] += 1         # back to 1 move
            diff[hi + limit + 1] += 1  # back to 2 moves

        # Prefix sum to get moves for each target t, find minimum
        ans = float('inf')
        cur = 0
        for t in range(2, 2 * limit + 1):
            cur += diff[t]
            ans = min(ans, cur)

        return ans
