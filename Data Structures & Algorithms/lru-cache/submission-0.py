class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.next = self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

        self.head, self.tail = Node(0,0), Node(0,0)
        self.head.next, self.tail.prev = self.tail, self.head

    def insert_head(self, node):
        prev, nxt = self.head, self.head.next
        prev.next = nxt.prev = node
        node.prev, node.next = prev, nxt
    
    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

        
    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert_head(self.cache[key])
            return self.cache[key].val
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert_head(self.cache[key])

        if len(self.cache) > self.capacity:
            tail = self.tail.prev
            self.remove(tail)
            self.cache.pop(tail.key)
        
