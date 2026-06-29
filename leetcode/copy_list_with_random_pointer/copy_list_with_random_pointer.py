"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        current = head

        newHead = Node(-1)
        copyCurrent = newHead

        lookup = {}

        while current is not None:
            newNode = Node(current.val)
            copyCurrent.next = newNode

            lookup[current] = newNode

            copyCurrent = copyCurrent.next
            current = current.next

        current = head
        copyCurrent = newHead.next

        while current is not None:
            if current.random is not None:
                copyCurrent.random = lookup[current.random]

            current = current.next
            copyCurrent = copyCurrent.next

        return newHead.next