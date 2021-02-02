# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root: TreeNode, low: int, high: int) -> TreeNode:
        fakeRoot = TreeNode(-10000000)
        fakeRoot.right = root
        Left = 0
        Right = 1

        def postorder(parent, child, node):
            if node is None:
                return

            postorder(node, Left, node.left)
            postorder(node, Right, node.right)

            if not (low <= node.val <= high):
                if node.left is not None and low <= node.left.val <= high:
                    if child == Left:
                        parent.left = node.left
                    else:
                        parent.right = node.left
                else:
                    if child == Left:
                        parent.left = node.right
                    else:
                        parent.right = node.right

        postorder(fakeRoot, Right, fakeRoot.right)
        return fakeRoot.right