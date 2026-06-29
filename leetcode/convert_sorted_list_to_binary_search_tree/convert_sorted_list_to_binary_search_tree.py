
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        def length(node):
            current = node
            count = 0

            while current is not None:
                current = current.next
                count += 1
            return count
        
        def get_bst(node):
            N = length(node)
            if N == 0:
                return None
            if N == 1:
                return TreeNode(node.val)

            previous = None
            middle = node
            for _ in range(N//2):
                previous = middle
                middle = middle.next

            if previous is not None:
                previous.next = None
            nxt = middle.next
            middle.next = None
            root = TreeNode(middle.val)
            root.left = get_bst(node)
            root.right = get_bst(nxt)
            return root
        return get_bst(head)