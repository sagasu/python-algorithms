class Solution:
    def isValid(self, s: str) -> bool:
        openParens = set(['(', '{', '['])
        closedParens = {
            '}': '{',
            ']': '[',
            ')': '('
        }

        stack = []

        for c in s:
            if c in openParens:
                stack.append(c)
            else:
                if c not in closedParens:
                    return False
                if len(stack) == 0 or stack[-1] != closedParens[c]:
                    return False
                stack.pop()

        return len(stack) == 0