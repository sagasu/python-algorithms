from collections import deque

class Solution(object):
    def reorderList(self, head):
        d = deque()
        curr = head
        
        # add all nodes to deque, remove .next association
        while curr:
            d.append(curr)
            temp = curr
            curr = curr.next
            temp.next = None
            
        left, right = None, None
        # popleft and pop, and connect them
        while len(d):
            left = d.popleft()
            if right:
                right.next = left
            
            # odd number of elements
            if not len(d):
                return
                
            right = d.pop()
            left.next = right