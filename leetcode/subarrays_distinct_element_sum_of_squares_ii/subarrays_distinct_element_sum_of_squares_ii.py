from typing import List


class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        """Sweep right endpoint r; Fenwick range-add on d[l] and add 2d+1 to the square sum."""
        MOD = 10**9 + 7
        n = len(nums)
        # Two Fenwick trees: D[i] and i*D[i] for range-add / range-sum of distinct counts.
        bit_d = [0] * (n + 2)
        bit_id = [0] * (n + 2)

        def add(bit, i, v):
            while i <= n:
                bit[i] += v
                i += i & -i

        def prefix(bit, i):
            s = 0
            while i > 0:
                s += bit[i]
                i -= i & -i
            return s

        def range_add(l, r, v):
            # 0-indexed inclusive [l, r] -> 1-indexed Fenwick
            l += 1
            r += 1
            add(bit_d, l, v)
            add(bit_d, r + 1, -v)
            add(bit_id, l, v * l)
            add(bit_id, r + 1, -v * (r + 1))

        def prefix_sum(i):
            # sum of d[0..i] inclusive (0-indexed)
            if i < 0:
                return 0
            j = i + 1
            return (j + 1) * prefix(bit_d, j) - prefix(bit_id, j)

        last = {}
        ans = 0
        sq = 0
        for r, x in enumerate(nums):
            l = last.get(x, -1) + 1
            s = prefix_sum(r) - prefix_sum(l - 1)
            sq += 2 * s + (r - l + 1)
            range_add(l, r, 1)
            last[x] = r
            ans += sq
        return ans % MOD


if __name__ == "__main__":
    s = Solution()
    tests = [
        ([1, 2, 1], 15),
        ([2, 2], 3),
    ]
    failed = False
    for nums, expected in tests:
        got = s.sumCounts(nums)
        if got == expected:
            print("OK")
        else:
            print("FAIL")
            failed = True
    if failed:
        raise SystemExit(1)
