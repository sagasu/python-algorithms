class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        def clone(node, to_clone):
            if not node: 
                return None
            
            if node in to_clone: 
                return to_clone[node]
            
            clone_node = Node(node.val)
            to_clone[node] = clone_node
            
            for neighbor in node.neighbors:
                to_clone[node].neighbors.append(clone(neighbor, to_clone))
            
            return clone_node
        
        return clone(node, {})