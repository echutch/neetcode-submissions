"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        old_new = {}
        queue = deque()
        old_new[node] = Node(node.val)
        queue.append(node)

        while queue:
            curr = queue.popleft()
            
            for next_node in curr.neighbors:
                if next_node not in old_new:
                    old_new[next_node] = Node(next_node.val)
                    queue.append(next_node)
                old_new[curr].neighbors.append(old_new[next_node])
        return old_new[node]



        