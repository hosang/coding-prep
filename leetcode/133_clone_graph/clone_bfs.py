# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, root):
        if root is None: return None
        old_to_new = {}
        todo = [root]
        while todo:
            old_node = todo.pop()
            if old_node not in old_to_new:
                old_to_new[old_node] = UndirectedGraphNode(old_node.label)
            new_node = old_to_new[old_node]
            
            for old_neighbor in old_node.neighbors:
                if old_neighbor not in old_to_new:
                    old_to_new[old_neighbor] = UndirectedGraphNode(old_neighbor.label)
                    todo.append(old_neighbor)
                new_node.neighbors.append(old_to_new[old_neighbor])
        return old_to_new[root]
        
