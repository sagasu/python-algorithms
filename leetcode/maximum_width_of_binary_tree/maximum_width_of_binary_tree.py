class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return 0
        level, res = [(root, 0)], 1
        while level:
            next_level = []
            res = max(res, level[-1][1] - level[0][1] + 1)
            for node, loc in level:
                if node.left:
                    next_level.append((node.left, 2 * loc))
                if node.right:
                    next_level.append((node.right, 2 * loc + 1))
            level = next_level
        return res