class WordFilter:

    def __init__(self, words: List[str]):
        self.lookup = {}
        for index, word in enumerate(words):
            N = len(word)
            rword = word[::-1]

            for i in range(1, N +1):
                for j in range(1, N +1):
                    self.lookup[(word[:i], rword[:j])] = index

    def f(self, prefix: str, suffix: str) -> int:
        suffix = suffix[::-1]
        if(prefix, suffix) in self.lookup:
            return self.lookup[(prefix, suffix)]
        return -1
