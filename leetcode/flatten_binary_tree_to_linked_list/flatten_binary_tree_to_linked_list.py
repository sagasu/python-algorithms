# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def preorder(node):
            if node.left is None and node.right is None:
                return node

            if node.right is None:
                last_node = preorder(node.left)
                node.right = node.left
                node.left = None
                return last_node

            if node.left is None:
                last_node = preorder(node.right)
                return last_node

            left_last_node = preorder(node.left)
            right_last_node = preorder(node.right)

            left_last_node.right = node.right
            node.right = node.left
            node.left = None
            return right_last_node

        if root is not None:
            preorder(root)