from __future__ import annotations


class Solution:
    def sortableIntegers(self, nums: list[int]) -> int:
        """Sum divisors k whose blocks are cyclic shifts of the matching sorted slices."""
        n = len(nums)
        target = sorted(nums)
        # Aligned blocks that end inside this prefix already equal their sorted slices.
        match_until = 0
        while match_until < n and nums[match_until] == target[match_until]:
            match_until += 1

        def blocks_rotate_to_sorted(k: int) -> bool:
            for start in range((match_until // k) * k, n, k):
                end = start + k
                descent = -1
                for i in range(start, end - 1):
                    if nums[i] > nums[i + 1]:
                        if descent != -1:
                            return False
                        descent = i
                if descent == -1:
                    for i in range(start, end):
                        if nums[i] != target[i]:
                            return False
                    continue
                # One drop, so the only candidate sort is the rotation starting after it.
                if nums[end - 1] > nums[start]:
                    return False
                src = descent + 1
                for i in range(start, end):
                    if nums[src] != target[i]:
                        return False
                    src += 1
                    if src == end:
                        src = start
            return True

        total = 0
        small = 1
        while small * small <= n:
            if n % small == 0:
                divisors = [small]
                if small * small != n:
                    divisors.append(n // small)
                for k in divisors:
                    if blocks_rotate_to_sorted(k):
                        total += k
            small += 1
        return total


if __name__ == "__main__":
    sol = Solution()
    tests = [
        ([3, 1, 2], 3),
        ([7, 6, 5], 0),
        ([5, 8], 3),
    ]
    failed = False
    for nums, expected in tests:
        got = sol.sortableIntegers(nums)
        if got == expected:
            print("OK")
        else:
            print("FAIL")
            failed = True
    if failed:
        raise SystemExit(1)
