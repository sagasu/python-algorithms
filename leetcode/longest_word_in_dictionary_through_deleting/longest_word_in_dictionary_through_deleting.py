class Solution:
    def findLongestWord(self, s: str, d: List[str]) -> str:
        lookup = collections.defaultdict(list)

        for index, word in enumerate(d):
            lookup[word[0]].append((index, 0))

        bestIndex = None
        for c in s:
            currentList = lookup[c][:]
            lookup[c].clear()
            for (wordIndex, charIndex) in currentList:
                if charIndex + 1< len(d[wordIndex]):
                    lookup[d[wordIndex][charIndex + 1]].append((wordIndex, charIndex + 1))
                else:
                    if bestIndex is None or len(d[wordIndex]) > len(d[bestIndex]) \
                         or (len(d[wordIndex]) == len(d[bestIndex]) and d[bestIndex] > d[wordIndex]):
                            bestIndex = wordIndex

        if bestIndex is None:
            return ""
        return d[bestIndex]