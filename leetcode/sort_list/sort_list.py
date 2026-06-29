class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        valAndNode = []
        while head:
            valAndNode.append((head.val, head))
            head = head.next
        valAndNode.sort(key=lambda x: x[0])
        for i in range(len(valAndNode)):
            valAndNode[i][1].next = valAndNode[i + 1][1] if i + 1 < len(valAndNode) else None
        return valAndNode[0][1] if len(valAndNode) else head