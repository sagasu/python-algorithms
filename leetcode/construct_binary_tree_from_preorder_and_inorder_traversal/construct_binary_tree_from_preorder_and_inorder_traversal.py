# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        N = len(preorder)
        preorder_index = 0
        inorder_index = {}
        for index, x in enumerate(inorder):
            inorder_index[x] = index

        root = TreeNode(preorder[preorder_index])
        preorder_index += 1

        def build(node, left, right):
            root_index = inorder_index[node.val]
            nonlocal preorder_index

            if root_index - 1 >= left:
                node.left = TreeNode(preorder[preorder_index])
                preorder_index += 1
                build(node.left, left, root_index -1)
            
            if right >= root_index + 1:
                node.right = TreeNode(preorder[preorder_index])
                preorder_index += 1
                build(node.right, root_index + 1, right)

        build(root, 0, N -1)
        return root