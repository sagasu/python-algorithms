from typing import List


class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        """Sort by digit sum then value; min swaps is n minus cycles in that permutation."""

        def digit_sum(x: int) -> int:
            s = 0
            while x:
                x, d = divmod(x, 10)
                s += d
            return s

        n = len(nums)
        target = sorted(nums, key=lambda x: (digit_sum(x), x))
        dest = {val: i for i, val in enumerate(target)}
        visited = [False] * n
        swaps = 0
        for i in range(n):
            if visited[i]:
                continue
            cycle_len = 0
            j = i
            while not visited[j]:
                visited[j] = True
                j = dest[nums[j]]
                cycle_len += 1
            swaps += cycle_len - 1
        return swaps


if __name__ == "__main__":
    s = Solution()
    tests = [
        ([37, 100], 1),
        ([22, 14, 33, 7], 0),
        ([18, 43, 34, 16], 2),
    ]
    failed = False
    for nums, expected in tests:
        got = s.minSwaps(nums)
        if got == expected:
            print("OK")
        else:
            print("FAIL")
            failed = True
    if failed:
        raise SystemExit(1)
