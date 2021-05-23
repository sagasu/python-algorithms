class Solution:
    def shortestSuperstring(self, words: List[str]) -> str:
        good_words = []
        for word in words:
            dominated = False
            for word2 in words:
                if word in word2 and word != word2:
                    dominated = True
            if not dominated:
                good_words.append(word)

        good_words.append("")
        N = len(good_words)

        overlap = [[-1] * N for _ in range(N)]
        for i in range(N):
            for j in range(N):
                overlap[i][j] = 0
                for k in range(1, len(good_words[i])):
                    if good_words[j].startswith(good_words[i][k:]):
                        overlap[i][j] = len(good_words[i]) - k
                        break
        cache = {}
        def get_subset(i, mask):
            if(mask == 0): return good_words[i]

            key =(i, mask)
            if key in cache:
                return cache[key]
            best_length = 300
            ans = "0" * 300
            debug = []
            for j in range(N):
                if(mask & (1 << j)) > 0:
                    c = overlap[i][j]
                    r = get_subset(j, mask ^ (1 << j))
                    current = good_words[i] + r[c:]

                    if len(current) < best_length:
                        best_length = len(current)
                        ans = current
            cache[key] = ans
            return ans

        return get_subset(N - 1, (1 << (N - 1)) - 1)