from __future__ import annotations


class Solution:
    def numOfWays(self, nums: list[int]) -> int:
        """Root is fixed first; left/right BST orders interleave by C(L+R, L). Exclude the original order."""
        MOD = 10**9 + 7
        n = len(nums)
        comb = [[0] * (n + 1) for _ in range(n + 1)]
        for i in range(n + 1):
            comb[i][0] = 1
            for j in range(1, i + 1):
                comb[i][j] = (comb[i - 1][j - 1] + comb[i - 1][j]) % MOD

        stack: list[tuple[list[int], bool]] = [(nums, False)]
        ways: list[int] = []
        while stack:
            arr, seen = stack.pop()
            if len(arr) <= 2:
                ways.append(1)
                continue
            if not seen:
                root = arr[0]
                left = [x for x in arr if x < root]
                right = [x for x in arr if x > root]
                stack.append((arr, True))
                stack.append((right, False))
                stack.append((left, False))
            else:
                right_ways = ways.pop()
                left_ways = ways.pop()
                left_n = sum(x < arr[0] for x in arr)
                right_n = len(arr) - 1 - left_n
                ways.append(
                    left_ways * right_ways % MOD * comb[left_n + right_n][left_n] % MOD
                )
        return (ways[0] - 1) % MOD


if __name__ == "__main__":
    s = Solution()
    tests = [
        ([2, 1, 3], 1),
        ([3, 4, 5, 1, 2], 5),
        ([1, 2, 3], 0),
    ]
    failed = False
    for nums, expected in tests:
        got = s.numOfWays(nums)
        if got == expected:
            print("OK")
        else:
            print("FAIL")
            failed = True
    if failed:
        raise SystemExit(1)
