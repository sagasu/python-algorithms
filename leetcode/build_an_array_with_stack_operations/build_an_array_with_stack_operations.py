class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        stack = [0]
        res = []
        for i in target:
            stack.append(i)
            if stack[-1] - stack[-2] == 1:
                res.append("Push")
            else:
                for j in range(stack[-1] - stack[-2] - 1):
                    res.append("Push")
                    res.append("Pop")
                res.append("Push")
        return res