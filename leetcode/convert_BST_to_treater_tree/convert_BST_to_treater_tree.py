# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        def inorder(node, sumTop):
            if node is None:
                return 0

            total = 0
            rightSum = inorder(node.right, sumTop)
            total += rightSum
            total += node.val
            node.val += rightSum + sumTop

            total += inorder(node.left, node.val)
            return total

        inorder(root, 0)
        return root