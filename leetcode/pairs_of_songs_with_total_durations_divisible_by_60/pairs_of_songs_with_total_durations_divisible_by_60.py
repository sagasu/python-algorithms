class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        N = len(time)
        counter = collections.Counter()
        total = 0

        for t in time:
            target = (60 - (t %60)) % 60
            total += counter[target]
            counter[t % 60] += 1

        return total