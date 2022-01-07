import random
class Solution(object):

    def __init__(self, head):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        :type head: ListNode
        """
        self.head = head
        self.vals = self.return_vals(self.head)
        
    def return_vals(self, head):
        vals = list()
        while head:
            vals.append(head.val)
            head = head.next
        return vals

    def getRandom(self):
        """
        Returns a random node's value.
        :rtype: int
        """
        rand = random.randint(0,len(self.vals)-1)
        return self.vals[rand]
            
# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()