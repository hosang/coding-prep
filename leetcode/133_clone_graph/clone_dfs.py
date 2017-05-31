# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    old_to_new = {}
    
    def cloneGraph(self, root):
        if root is None: return None
        if root in self.old_to_new:
            return self.old_to_new[root]
            
        new_node = self.old_to_new[root] = UndirectedGraphNode(root.label)
        for neighbor in root.neighbors:
            new_node.neighbors.append(self.cloneGraph(neighbor))
        return new_node
