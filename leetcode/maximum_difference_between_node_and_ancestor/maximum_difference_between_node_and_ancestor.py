class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def dfs(root, mn, mx):
            if not root: return 0
            res = max(abs(root.val - mn), abs(root.val - mx))
            mn, mx = min(mn, root.val), max(mx, root.val)
            return max(res, dfs(root.left, mn, mx), dfs(root.right, mn, mx))
        
        return dfs(root, root.val, root.val)