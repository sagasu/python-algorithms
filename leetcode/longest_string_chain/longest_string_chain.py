class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=lambda x: len(x))
        best = 0
        dp = {}

        for word in words:
            best_prev = 0

            for index in range(len(word)):
                prev_word = word[:index] + word[index + 1:]
                if prev_word in dp:
                    best_prev = max(best_prev, dp[prev_word])

            dp[word] = best_prev + 1
        return max(dp.values())