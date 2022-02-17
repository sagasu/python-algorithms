class Solution:
    def combinationSum(self, candidates, target):
        res = []
        candidates.sort()
        def dfs(remain, stack):
            if not remain:
                res.append(stack)
                return 
            for item in candidates:
                if item > remain:
                    break
                elif not stack or item >= stack[-1]:
                    dfs(remain - item, stack + [item])
        dfs(target, [])
        return res