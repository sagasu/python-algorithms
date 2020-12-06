class Solution:
    def connect(self, root: 'Node') -> 'Node':
        level = []
        if root is not None:
            level = [root]
        
        while len(level) > 0:
            next_level = []

            for previous_node, node in zip(level, level[1:]):
                previous_node.next = node

            for node in level:
                if node.left is not None:
                    next_level.append(node.left)
                if node.right is not None:
                    next_level.append(node.right)

            level = next_level
        return root