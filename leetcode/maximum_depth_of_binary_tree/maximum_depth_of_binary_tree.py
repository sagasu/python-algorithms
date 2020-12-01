class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        def depth(node):
            if node is None:
                return 0

            leftDepth = depth(node.left) 
            rightDepth = depth(node.right) 

            return max(leftDepth, rightDepth) + 1

        return depth(root)