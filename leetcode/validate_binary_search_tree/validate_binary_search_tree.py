class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def dfs(node):
            if node is None:
                return (True, None, None)

            leftIsValid, leftSmallest, leftLargest = dfs(node.left)
            rightIsValid, rightSmallest, rightLargest = dfs(node.right)

            leftIsSmallest = (leftLargest is None) or leftLargest < node.val
            rightIsBigger = (rightSmallest is None) or rightSmallest > node.val

            if leftSmallest is not None:
                smallest = leftSmallest
            else:
                smallest = node.val

            if rightLargest is not None:
                largest = rightLargest
            else:
                largest = node.val

            isValid = leftIsValid and rightIsValid and leftIsSmallest and rightIsBigger

            return (isValid, smallest, largest)

        isValid, _, _ = dfs(root)
        return isValid