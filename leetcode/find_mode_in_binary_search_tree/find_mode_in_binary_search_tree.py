from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        def h(node,l):
            if node is None:
                return l
            if(node.val in l):
                l[node.val]+=1
            else:
                l[node.val]=1
            if(node.left is not None):
                h(node.left,l)
            if(node.right is not None):
                h(node.right,l)
            return l
        
        dic=dict()
        h(root,dic)
        m=max(dic.values())
        return (i for i,v in dic.items() if(v==m))