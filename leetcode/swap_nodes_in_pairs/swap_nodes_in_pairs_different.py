class Solution:
    def swapPairs(self, h):
        if h and not h.next:
            return h
        l = d = ListNode('dummy')
        while h and h.next:
            r = h.next.next
            l.next = t = h.next
            t.next = l = h
            l.next = h = r
        return d.next