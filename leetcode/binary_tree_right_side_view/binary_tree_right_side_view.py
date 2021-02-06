# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        ans = []

        def preorder(node, depth):
            if node is None:
                return

            if len(ans) <= depth:
                ans.append(node.val)

            preorder(node.right, depth + 1)
            preorder(node.left, depth +1)

        preorder(root, 0)
        return ans