class Solution:
    def sumOfLeftLeaves(self, root):
        if not root:
            return 0
        else:
            if root.left and not root.left.left and not root.left.right:
                return root.left.val + self.sumOfLeftLeaves(root.right)
            else:
                return self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)