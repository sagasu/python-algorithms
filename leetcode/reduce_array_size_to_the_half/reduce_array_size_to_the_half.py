class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        N = len(arr)
        freq = collections.Counter(arr)
        removed = 0
        count = 0

        for v in sorted(freq.values(), reverse=True):
            removed += v
            count += 1

            if removed * 2 >= N:
                return count

        return 0