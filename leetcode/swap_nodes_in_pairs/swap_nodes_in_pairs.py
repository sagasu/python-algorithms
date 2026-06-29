class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        
        dummy=tmp=ListNode(0,head)
        
        curr=head

        while(curr and curr.next):
            t=curr.next.next
            n=curr.next
            curr.next=None
            n.next=curr
            tmp.next=n
            tmp=tmp.next.next
            curr.next=t
            curr=curr.next
            
        return dummy.next