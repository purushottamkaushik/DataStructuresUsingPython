"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""




class Solution:
    def __init__(self):
        self.visited = {}
    
    def cloneGraph(self, node: 'Node') -> 'Node':
        
        
        # if node is not there so return the node
        if not node:
            return node
        
        # if Node exists in visited list then return the value of the node 
        if node in self.visited:
            return self.visited[node]
        
        # create new node if it doesnt exists in the visited hashtable 
        # with initially empty neighbours
        new_node = Node(node.val,[])
        
        self.visited[node] = new_node
        
        if node.neighbors:
            new_node.neighbors = [self.cloneGraph(n) for n in node.neighbors]
        
        return new_node
            
        
        
        
        
        