class Node:
    def __init__(self):
        self.edges = {}
        self.words = []

    def add(self, word):
        self.words.append(word)
        self.words.sort()

        if len(self.words) > 3:
            self.words.pop()
    
class Trie:
    def __init__(self):
        self.root = Node()

    def add(self, word):
        current = self.root

        for c in word:
            if c not in current.edges:
                current.edges[c] = Node()

            current.add(word)
            current = current.edges[c]

        current.add(word)

    def searchWithPrefix(self, word):
        ans = []
        current = self.root

        for c in word:
            if c not in current.edges:
                break

            current = current.edges[c]
            ans.append(current.words)

        while len(ans) < len(word):
            ans.append([])

        return ans

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        t = Trie()

        for product in products:
            t.add(product)

        return t.searchWithPrefix(searchWord)