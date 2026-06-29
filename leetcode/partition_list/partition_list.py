class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        small_half = ListNode(-1)
        small_half_tail = small_half
        big_half = ListNode(-1)
        big_half_tail = big_half

        current = head
        while current is not None:
            if current.val >= x:
                big_half_tail.next = current
                big_half_tail = big_half_tail.next
            else:
                small_half_tail.next = current
                small_half_tail = small_half_tail.next
            current = current.next

        small_half_tail.next = big_half.next
        big_half_tail.next = None

        return small_half.next
        
