class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        N = len(S)
        S = S.lower()
        ans = []

        def generate(index, current):
            if index == N:
                ans.append(current)
                return
            
            if S[index].isalpha():
                generate(index + 1, current + S[index].lower())
                generate(index + 1, current + S[index].upper())
            else:
                generate(index + 1, current + S[index])

        generate(0, "")
        return ans