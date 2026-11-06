class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.data = [0] * capacity
        self.size = 0

    def get(self, i: int) -> int:
        return self.data[i]


    def set(self, i: int, n: int) -> None:
        self.data[i] = n


    def pushback(self, n: int) -> None:
        if self.size == self.capacity:
            self.resize()
        self.data[self.size] = n
        self.size += 1


    def popback(self) -> int:
        self.size -= 1
        return self.data[self.size]
 

    def resize(self) -> None:
        double = 2 * self.capacity

        while self.capacity < double:
            self.data.append(0)
            self.capacity += 1


    def getSize(self) -> int:
        return self.size
        
    
    def getCapacity(self) -> int:
        return self.capacity
