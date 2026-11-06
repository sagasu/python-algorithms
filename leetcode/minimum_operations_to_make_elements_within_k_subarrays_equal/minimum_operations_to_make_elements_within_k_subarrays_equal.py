from typing import List


class Solution:
    def minOperations(self, nums: List[int], x: int, k: int) -> int:
        """Median cost of every length-x window (Fenwick) then DP over k non-overlapping windows."""
        n = len(nums)
        vals = sorted(set(nums))
        rank = {v: i + 1 for i, v in enumerate(vals)}
        m = len(vals)
        cnt = [0] * (m + 1)
        sm = [0] * (m + 1)

        def add(i: int, dc: int, ds: int) -> None:
            while i <= m:
                cnt[i] += dc
                sm[i] += ds
                i += i & -i

        def prefix_cnt(i: int) -> int:
            s = 0
            while i > 0:
                s += cnt[i]
                i -= i & -i
            return s

        def prefix_sm(i: int) -> int:
            s = 0
            while i > 0:
                s += sm[i]
                i -= i & -i
            return s

        def kth(kth_i: int) -> int:
            idx = 0
            mask = 1 << (m.bit_length() - 1)
            while mask:
                nxt = idx + mask
                if nxt <= m and cnt[nxt] < kth_i:
                    idx = nxt
                    kth_i -= cnt[nxt]
                mask >>= 1
            return idx + 1

        window_sum = 0
        costs = [0] * (n - x + 1)
        for i, v in enumerate(nums):
            add(rank[v], 1, v)
            window_sum += v
            if i >= x:
                old = nums[i - x]
                add(rank[old], -1, -old)
                window_sum -= old
            if i >= x - 1:
                idx = kth((x + 1) // 2)
                median = vals[idx - 1]
                less_c = prefix_cnt(idx - 1)
                less_s = prefix_sm(idx - 1)
                med_c = prefix_cnt(idx) - less_c
                greater_c = x - less_c - med_c
                greater_s = window_sum - less_s - median * med_c
                costs[i - x + 1] = median * less_c - less_s + greater_s - median * greater_c

        inf = 10**18
        prev = [0] * (n + 1)
        for _ in range(k):
            cur = [inf] * (n + 1)
            for i in range(1, n + 1):
                best = cur[i - 1]
                if i >= x:
                    cand = prev[i - x] + costs[i - x]
                    if cand < best:
                        best = cand
                cur[i] = best
            prev = cur
        return prev[n]


if __name__ == "__main__":
    sol = Solution()
    tests = [
        ([5, -2, 1, 3, 7, 3, 6, 4, -1], 3, 2, 8),
        ([9, -2, -2, -2, 1, 5], 2, 2, 3),
    ]
    failed = False
    for nums, x, k, expected in tests:
        got = sol.minOperations(nums, x, k)
        if got == expected:
            print("OK")
        else:
            print("FAIL")
            failed = True
    if failed:
        raise SystemExit(1)
