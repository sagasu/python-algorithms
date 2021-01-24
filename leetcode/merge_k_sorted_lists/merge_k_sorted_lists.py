# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        setattr(ListNode, "__lt__", lambda self, other: self.val <= other.val)

        head = ListNode(-1)
        tail = head

        heap = []
        for listHead in lists:
            if listHead is not None:
                heapq.heappush(heap, listHead)

        while len(heap) > 0:
            listHead = heap[0]
            heapq.heappop(heap)

            tail.next = listHead

            if listHead.next is not None:
                nextNode = listHead.next
                heapq.heappush(heap, nextNode)

            listHead.next = None
            tail = tail.next

        return head.next