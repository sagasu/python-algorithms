class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        d = set()

        def generate(n):
            if n == 0:
                return [""]

            ans = []
            for left in range(n):
                right = n - left - 1
                leftParens = generate(left)
                rightParens = generate(right)

                for leftP in leftParens:
                    for rightP in rightParens:
                        ans.append(leftP + "(" + rightP + ")")
            return ans
        return generate(n)