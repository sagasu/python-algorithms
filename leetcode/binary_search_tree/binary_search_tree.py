

class Solution:
    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if root == None:
            return TreeNode(val)
        p = root
        while p:
            if val < p.val: 
                if p.left:
                    p = p.left
                else:
                    p.left = TreeNode(val)
                    break
            else:
                if p.right:
                    p = p.right
                else:
                    p.right = TreeNode(val)
                    break
        return root