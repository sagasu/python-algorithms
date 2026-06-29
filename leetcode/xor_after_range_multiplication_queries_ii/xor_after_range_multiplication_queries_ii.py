from typing import List
from functools import reduce
from operator import xor
import math

MOD = 10**9 + 7


class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(nums)
        B = int(math.isqrt(n)) + 1

        # For each small stride k, and each residue r (0..k-1),
        # the positions with that stride+residue are: r, r+k, r+2k, ...
        # Map them to a virtual array of length ceil((n-r)/k).
        # Use a difference array on this virtual array for range-multiply queries.
        # Query (l, rq, k, v): residue r=l%k, virtual start=l//k... actually start=(l-r)//k
        # virtual end = (rq - r) // k  (since rq >= l and rq%k may differ)
        # Wait: positions hit are l, l+k, ..., rq. These all have residue l%k.
        # Virtual index of position p = (p - r) // k where r = l % k.
        # So virtual start = (l - r) // k, virtual end = (rq - r) // k
        # (rq might not be ≡ r mod k, but the last hit position is rq - (rq-r)%k... 
        #  actually the last hit is min(rq, last p <= rq with p≡r mod k))

        # diff[k][r] = difference array for stride k, residue r
        # Length = ceil((n - r) / k) + 1

        inv_cache = {}
        def modinv(v):
            if v not in inv_cache:
                inv_cache[v] = pow(v, MOD - 2, MOD)
            return inv_cache[v]

        # Use dict of dicts: diff[k][r] = list
        from collections import defaultdict
        diff = defaultdict(lambda: defaultdict(lambda: None))

        for l, rq, k, v in queries:
            if k > B:
                for idx in range(l, rq + 1, k):
                    nums[idx] = nums[idx] * v % MOD
            else:
                r = l % k
                # virtual indices: vl = (l - r) // k, vr = last position <= rq with pos%k==r
                last_pos = rq - (rq - r) % k if rq >= r else -1
                if last_pos < l:
                    continue
                vl = (l - r) // k
                vr = (last_pos - r) // k
                vlen = (n - r + k - 1) // k  # total virtual length for this (k, r)

                if diff[k][r] is None:
                    diff[k][r] = [1] * (vlen + 1)
                d = diff[k][r]
                d[vl] = d[vl] * v % MOD
                if vr + 1 <= vlen:
                    d[vr + 1] = d[vr + 1] * modinv(v) % MOD

        # Apply difference arrays back to nums
        for k, res_dict in diff.items():
            for r, d in res_dict.items():
                if d is None:
                    continue
                cur = 1
                vi = 0
                pos = r
                while pos < n:
                    cur = cur * d[vi] % MOD
                    if cur != 1:
                        nums[pos] = nums[pos] * cur % MOD
                    pos += k
                    vi += 1

        return reduce(xor, nums)
