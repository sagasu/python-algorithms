class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        walker = dummy = ListNode(0)
        dummy.next = head
        while walker:
            runner = walker.next
            while runner and runner.next and runner.val == runner.next.val:
                runner = runner.next
            if walker.next is runner:
                walker = walker.next
            else:
                walker.next = runner.next
        return dummy.next