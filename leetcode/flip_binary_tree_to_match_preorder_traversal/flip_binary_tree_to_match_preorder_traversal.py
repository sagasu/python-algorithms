class Solution:
    def flipMatchVoyage(self, root: TreeNode, voyage: List[int]) -> List[int]:
        N = len(voyage)
        index = 0
        impossible = False
        swaps = []

        def preorder(node):
            if node is None:
                return
            
            nonlocal index
            if node.val != voyage[index]:
                nonlocal impossible
                impossible = True
                return
            index += 1

            if node.right is not None and node.right.val == voyage[index] and node.left is not None:
                swaps.append(node.val)
                preorder(node.right)
                preorder(node.left)
            else:
                preorder(node.left)
                preorder(node.right)

        preorder(root)

        if impossible:
            return[-1]
        return swaps