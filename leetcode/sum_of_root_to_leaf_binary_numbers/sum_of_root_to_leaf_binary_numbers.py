class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        def sumRootToLeaf(r, s):
            li, x = [n for n in [r.left, r.right] if n], (s << 1) + r.val
            return x if not li else sum(sumRootToLeaf(n, x) for n in li)
        return sumRootToLeaf(root, 0)