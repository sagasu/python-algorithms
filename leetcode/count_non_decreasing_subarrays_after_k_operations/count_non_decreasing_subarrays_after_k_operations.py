from collections import deque
from typing import List


class Solution:
    # Reverse so adding on the right updates suffix maxima; slide left while cost > k.
    def countNonDecreasingSubarrays(self, nums: List[int], k: int) -> int:
        a = nums[::-1]
        n = len(a)
        dq = deque()
        ops = 0
        left = 0
        ans = 0
        for right in range(n):
            cnt = 1
            while dq and dq[-1][0] <= a[right]:
                h, c = dq.pop()
                cnt += c
                ops += (a[right] - h) * c
            dq.append([a[right], cnt])
            while ops > k:
                dq[0][1] -= 1
                ops -= dq[0][0] - a[left]
                if dq[0][1] == 0:
                    dq.popleft()
                left += 1
            ans += right - left + 1
        return ans


if __name__ == "__main__":
    sol = Solution()
    tests = [
        ([6, 3, 1, 2, 4, 4], 7, 17),
        ([6, 3, 1, 3, 6], 4, 12),
    ]
    failed = False
    for nums, k, expected in tests:
        got = sol.countNonDecreasingSubarrays(nums, k)
        if got == expected:
            print("OK")
        else:
            print("FAIL")
            failed = True
    if failed:
        raise SystemExit(1)
