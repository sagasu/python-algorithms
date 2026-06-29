class Solution:
    def __init__(self):
        self.counter = itertools.count()
        
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        pq = [(n.val, next(self.counter), n) for n in lists if n]
        heapq.heapify(pq)
        
        dummy = node = ListNode(0)
        while pq:
            val, count, n = heapq.heappop(pq)
            if n.next:
                heapq.heappush(pq, (n.next.val, next(self.counter), n.next))

            node.next = n
            node = n
        
        return dummy.next