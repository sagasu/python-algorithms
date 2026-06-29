class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        pushed = collections.deque(pushed)
        stack = []

        for x in popped:
            if len(stack) > 0 and x == stack[-1]:
                stack.pop()
                continue

            while len(pushed) > 0 and pushed[0] != x:
                stack.append(pushed[0])
                pushed.popleft()

            if len(pushed) == 0:
                return False

            pushed.popleft()
        return True