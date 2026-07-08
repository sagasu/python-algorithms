from typing import List

MOD = 10**9 + 7
_MX = 10**5 + 1
_POW10 = [1] * _MX
for _i in range(1, _MX):
    _POW10[_i] = _POW10[_i - 1] * 10 % MOD


class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        n = len(s)
        # Prefix over first i chars: digit sum, non-zero count, concatenated value mod MOD
        sum_d = [0] * (n + 1)
        cnt_nz = [0] * (n + 1)
        pref = [0] * (n + 1)

        for i, ch in enumerate(s, 1):
            d = ord(ch) - 48
            sum_d[i] = sum_d[i - 1] + d
            if d:
                cnt_nz[i] = cnt_nz[i - 1] + 1
                pref[i] = (pref[i - 1] * 10 + d) % MOD
            else:
                cnt_nz[i] = cnt_nz[i - 1]
                pref[i] = pref[i - 1]

        ans = []
        for l, r in queries:
            nz = cnt_nz[r + 1] - cnt_nz[l]
            sd = sum_d[r + 1] - sum_d[l]
            # pref[r+1] = pref[l] * 10^nz + x  (mod MOD)
            x = (pref[r + 1] - pref[l] * _POW10[nz] % MOD) % MOD
            ans.append(x * sd % MOD)
        return ans
