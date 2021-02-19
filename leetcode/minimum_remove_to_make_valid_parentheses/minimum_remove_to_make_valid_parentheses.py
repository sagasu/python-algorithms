class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []

        bad = set()

        for index, c in enumerate(s):
            if c == "(":
                stack.append(index)
            elif c == ")":
                if len(stack) > 0:
                    stack.pop()
                else:
                    bad.add(index)

        for leftover in stack:
            bad.add(leftover)


        return "".join(c for index, c in enumerate(s) if index not in bad)