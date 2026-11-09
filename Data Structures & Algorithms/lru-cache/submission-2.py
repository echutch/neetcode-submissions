class Node:
    def __init__(self, key, next=None, prev=None):
        self.key = key
        self.next = next
        self.prev = prev

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.map_key = {}
        self.head = None # MRU
        self.tail = None # LRU
        

    def get(self, key: int) -> int:
        if key not in self.map_key:
            return -1

        self.use(key)
        return self.map_key[key]


    def put(self, key: int, value: int) -> None:
        if key in self.map_key:
            self.use(key)
        else:
            new_node = Node(key, self.head, None)
            
            if self.head:
                self.head.prev = new_node
            self.head = new_node
            self.size += 1

            if not self.tail:
                self.tail = new_node

            if self.size > self.capacity:
                self.map_key.pop(self.tail.key)
                self.tail = self.tail.prev
                self.tail.next = None
                self.size -= 1
        self.map_key[key] = value
        


    def use(self, key):
        if self.head.key == key:
            return True

        curr = self.head

        while curr:
            if curr.key == key:
                curr.prev.next = curr.next
                if curr.next:
                    curr.next.prev = curr.prev
                if self.tail == curr:
                    self.tail = curr.prev

                curr.next = self.head
                self.head.prev = curr
                curr.prev = None
                self.head = curr
                return True
            prev = curr
            curr = curr.next

        return False
                
        
