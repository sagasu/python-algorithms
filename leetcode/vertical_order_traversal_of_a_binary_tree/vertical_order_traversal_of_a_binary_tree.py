# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        xs = collections.defaultdict(list)

        def preorder(node, x, y):
            if node is None:
                return


            xs[x].append((-y, node.val))

            preorder(node.left, x -1, y-1)
            preorder(node.right, x + 1, y-1)

        preorder(root, 0, 0)

        ans = []
        for key in sorted(xs.keys()):
            ans.append(list(val for _, val in sorted(xs[key])))

        return ans