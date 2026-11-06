"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        map_rand = {}

        curr = head
        dummy = prev = Node(0, None, None)
        while curr:
            new_node = Node(curr.val, None, None)
            
            prev.next = new_node
            prev = prev.next

            map_rand[curr] = new_node
            curr = curr.next
        
        for old, new in map_rand.items():
            if not old.random:
                new.random = None
            else:
                new.random = map_rand[old.random]

        return dummy.next
            
        