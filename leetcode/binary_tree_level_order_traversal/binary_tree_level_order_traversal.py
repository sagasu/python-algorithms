# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        traversal = []
        q = collections.deque()
        def queue(node, level):
            if node is not None:
                q.append((node, level))
        queue(root, 0)

        while len(q)>0:
            node,level = q.popleft()
            if len(traversal) == level:
                traversal.append([])
            traversal[level].append(node.val)

            queue(node.left, level +1)
            queue(node.right, level +1)
        return traversal