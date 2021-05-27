class Solution:
    def maxProduct(self, words: List[str]) -> int:
        N = len(words)
        mask = []
        sets = []

        def calculateMask(word):
            mask = 0

            for c in word:
                offset = ord(c) - ord('a')
                mask |= (1 << offset)
            return mask

        def calculateSet(word):
            s = [False] * 26
            for c in word:
                offset = ord(c) - ord('a')
                s[offset] |= True

            return s

        for word in words:
            mask.append(calculateMask(word))

        for word in words:
            sets.append(calculateSet(word))

        mx = 0
        for i in range(N):
            for j in range(i+1, N):
                # if(mask[i] & mask[j] == 0):
                #     mx = max(mx, len(words[i]) * len(words[j]))
                if sum(1 for a,b in zip(sets[i], sets[j]) if a and b) == 0:
                    mx = max(mx, len(words[i]) * len(words[j]))
        return mx