class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        indices = collections.defaultdict(list)

        for index, c in enumerate(s):
            indices[c].append(index)

        def matching(word):
            last = -1
            for c in word:
                index = bisect.bisect_right(indices[c], last)
                if index >= len(indices[c]):
                    return False

                last = indices[c][index]
            return True
        
        count = 0
        for word in words:
            if matching(word):
                count += 1
        return count