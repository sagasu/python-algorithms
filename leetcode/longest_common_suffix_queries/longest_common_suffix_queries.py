from typing import List


class Solution:
    def stringIndices(self, wordsContainer: List[str], wordsQuery: List[str]) -> List[int]:
        # Build a trie of reversed wordsContainer strings.
        # Each node stores the best (shortest, then smallest index) word index
        # that passes through it.
        
        # Trie node: [children dict, best_index]
        # best_index = index of shortest word in wordsContainer that has this suffix
        root = [{}, -1]

        def better(a: int, b: int) -> int:
            """Return the index of the better word (shorter, tie-break by smaller index)."""
            if a == -1:
                return b
            if b == -1:
                return a
            la, lb = len(wordsContainer[a]), len(wordsContainer[b])
            if la != lb:
                return a if la < lb else b
            return min(a, b)

        # Insert all wordsContainer reversed
        for i, word in enumerate(wordsContainer):
            node = root
            node[1] = better(node[1], i)
            for c in reversed(word):
                if c not in node[0]:
                    node[0][c] = [{}, -1]
                node = node[0][c]
                node[1] = better(node[1], i)

        # Answer each query
        ans = []
        for word in wordsQuery:
            node = root
            for c in reversed(word):
                if c not in node[0]:
                    break
                node = node[0][c]
            ans.append(node[1])

        return ans
