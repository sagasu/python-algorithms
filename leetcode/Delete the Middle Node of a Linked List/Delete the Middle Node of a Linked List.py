from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return None
        
        # Dummy node to handle edge cases
        dummy = ListNode(0, head)
        slow = dummy
        fast = head
        
        # Move fast twice as fast as slow
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Delete the middle node
        slow.next = slow.next.next
        
        return dummy.next