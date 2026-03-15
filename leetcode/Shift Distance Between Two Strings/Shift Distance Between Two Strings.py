from typing import List


class Solution:
    def shiftDistance(self, s: str, t: str, nextCost: List[int], previousCost: List[int]) -> int:
        # Build prefix sums over a doubled alphabet (indices 0..51)
        # so we can handle wrap-around (e.g. z -> a) without modular arithmetic per query.
        # s1[i] = cumulative forward-shift cost from 'a' up to index i
        # s2[i] = cumulative backward-shift cost from 'a' up to index i
        m = 26
        s1 = [0] * (m * 2 + 1)
        s2 = [0] * (m * 2 + 1)
        for i in range(m * 2):
            s1[i + 1] = s1[i] + nextCost[i % m]
            s2[i + 1] = s2[i] + previousCost[(i + 1) % m]

        ans = 0
        for a, b in zip(s, t):
            x, y = ord(a) - ord('a'), ord(b) - ord('a')
            # Forward cost: x -> x+1 -> ... -> y (wrap if y < x)
            forward = s1[y + m if y < x else y] - s1[x]
            # Backward cost: x -> x-1 -> ... -> y (wrap if x < y)
            backward = s2[x + m if x < y else x] - s2[y]
            ans += min(forward, backward)

        return ans
