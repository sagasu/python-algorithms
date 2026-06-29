class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = []
        start = -1
        best = 0

        for index, c in enumerate(s):
            if c == "(":
                stack.append(index)
            else:
                if len(stack) == 0:
                    start = index
                    continue
                stack.pop()
                if len(stack) > 0:
                    best = max(best, index - stack[-1])
                else:
                    best = max(best, index - start)

        return best