class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        if head == None:
            return None
        fast=slow=head
        while fast != None:
            fast=fast.next
            if fast != None:
                fast=fast.next
            elif fast==None:
                return slow
            slow=slow.next
        return slow