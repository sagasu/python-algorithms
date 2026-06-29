"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Node') -> 'Node':

        def flat(node):
            current = node

            while current is not None:
                if current.child is not None:
                    oldNext = current.next
                    current.next = current.child

                    oldChild = current.child
                    oldChild.prev = current

                    current.child = None
                    newEnd = flat(oldChild)

                    newEnd.next = oldNext
                    if oldNext is not None:
                        oldNext.prev = newEnd

                if current.next is None:
                    return current
                current = current.next
            return None

        flat(head)
        return head

            