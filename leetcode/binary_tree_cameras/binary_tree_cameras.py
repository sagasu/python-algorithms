# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minCameraCover(self, root: TreeNode) -> int:
        cache = collections.defaultdict(int)
        inf = 10 ** 10 

        def cover(node, needed, parent):
            if node is None:
                return 0

            key = (node, needed, parent)
            if key in cache:
                return cache[key]

            best = inf
            if needed:
                ans = (cover(node.left, False, True) + cover(node.right, False, True)) + 1
                best = min(ans, best)
            else:
                if parent:
                    ans = (cover(node.left, False, False) + cover(node.right, False, False))
                    best = min(ans, best)

                    ans = (cover(node.left, False, True) + cover(node.right, False, True) + 1)
                    best = min(ans, best)
                else:
                    if node.left is not None:
                        ans = cover(node.left, True, False) + cover(node.right, False, False)
                        best = min(ans, best)
                        
                    if node.right is not None:
                        ans = cover(node.left, False, False) + cover(node.right, True, False)
                        best = min(ans, best)
                    ans = (cover(node.left, False, True) + cover(node.right, False, True) + 1)
                    best = min(ans, best)
            cache[key] = best
            return cache[key]
        return cover(root, False, False)


