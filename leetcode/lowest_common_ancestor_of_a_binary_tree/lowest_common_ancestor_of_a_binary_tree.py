# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def find(node, target):
            if node is None:
                return (False, [])

            if node.val == target.val:
                return (True, [node])
            left = find(node.left, target)
            if left[0]:
                return (True, [node] + left[1])
            right = find(node.right, target)
            if right[0]:
                return (True, [node] + right[1])

            return (False, [])

        _, ppath = find(root, p)
        _, qpath = find(root, q)

        last = root
        for pn, qn in zip(ppath, qpath):
            if pn.val != qn.val:
                return last
            last = pn
        return last