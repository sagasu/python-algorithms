from typing import Optional


class Definition:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

ListNode = Definition


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head

        # Find length and tail
        length = 1
        tail = head
        while tail.next:
            tail = tail.next
            length += 1

        k %= length
        if k == 0:
            return head

        # Find new tail: (length - k - 1) steps from head
        new_tail = head
        for _ in range(length - k - 1):
            new_tail = new_tail.next

        new_head = new_tail.next
        new_tail.next = None
        tail.next = head  # make circular then break

        return new_head
