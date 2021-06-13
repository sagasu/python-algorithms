class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        lookup = {}
        for index, word in enumerate(words):
            lookup[word] = index
        ans = set()
        for index, word in enumerate(words):
            for k in range(len(word) + 1):
                current = word[:k][::-1]

                if current in lookup and lookup[current] != index :
                    newword = word + current

                    if newword == newword[::-1]:
                        ans.add((index, lookup[current]))

                current = word[len(word) - k:][::-1]
                if current in lookup and lookup[current]!=index:
                    newword = current + word
                    if newword == newword[::-1]:
                        ans.add((lookup[current], index))
        return list(ans)