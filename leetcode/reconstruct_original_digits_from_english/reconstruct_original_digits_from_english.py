class Solution:
    def originalDigits(self, s: str) -> str:
        f = collections.Counter(s)

        mappings = list(pair.split(" ") for pair in """0 zero,6 six,4 four,5 five,7 seven,2 two,8 eight,1 one,9 nine,3 three""".split(","))

        ans = []
        for digit, word in mappings:
            freq_char = collections.Counter(word)

            min_overlap = float("inf")

            for c in freq_char.keys():
                min_overlap = min(min_overlap, f[c] // freq_char[c])

            for c in freq_char.keys():
                f[c] -= min_overlap

            ans.append(digit * min_overlap)

        ans.sort()
        return "".join(ans)