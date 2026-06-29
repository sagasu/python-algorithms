from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def __init__(self):
        self.largestVals = []

    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        self.setLargestValues(root, 0)
        return self.largestVals

    def setLargestValues(self, root: TreeNode, level: int):
        if(root == None): return
        if(len(self.largestVals) > level):
            self.largestVals[level] = max(self.largestVals[level], root.val)
        else:
            self.largestVals.append(root.val)

        self.setLargestValues(root.left, level+1)
        self.setLargestValues(root.right, level+1)


tree = TreeNode(1,TreeNode(3,TreeNode(5),TreeNode(3)), TreeNode(2,TreeNode(9)))
largestVal = Solution().largestValues(tree)
print(largestVal)

print(Solution().largestValues(TreeNode(1,TreeNode(2), TreeNode(3))))
