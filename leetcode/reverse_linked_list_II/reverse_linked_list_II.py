# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        left -= 1
        right -= 1

        newHead = ListNode(-1)
        newHead.next = head
        
        deque = collections.deque()
        current = newHead.next

        for index in range(right + 1):
            if left <= index <= right:
                deque.append(current)
            current = current.next

        while len(deque) >= 2:
            front = deque.popleft()
            back = deque.pop()

            front.val, back.val = back.val, front.val
        return newHead.next
