class Solution:
    def getAllElements(self, A: TreeNode, B: TreeNode) -> List[int]:
        l=[]
        def flat(T):
            if T:
                l.append(T.val)
                flat(T.left)
                flat(T.right)
        flat(A)
        flat(B)
        return sorted(l)