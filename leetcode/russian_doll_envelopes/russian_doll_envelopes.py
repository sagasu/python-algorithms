class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key=lambda e:(e[0], -e[1]))
        N = len(envelopes)

        best = [0]
        for _, h in envelopes:
            index = bisect.bisect_left(best, h)

            if index == len(best):
                best.append(h)
            else:
                best[index] = h

        return len(best) - 1