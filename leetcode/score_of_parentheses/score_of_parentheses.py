class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        stack = []

        for c in S:
            if c == "(":
                stack.append("(")
                continue

            if c ==")":
                if len(stack) > 0 and stack[-1] == "(":
                    stack.pop()
                    stack.append(1)
                    continue

                total = 0
                while len(stack) > 0 and stack[-1] != "(":
                    total += stack[-1]
                    stack.pop()

                total *= 2
                stack.pop()
                stack.append(total)

        return sum(stack)