import heapq
class MedianFinder:

    def __init__(self):
        self.max = []
        self.min = []

    # max: [2, 1]  
    # min: [3]

    def addNum(self, num: int) -> None:
        if not self.min or num > self.min[0]:
            heapq.heappush(self.min, num)
        else:
            heapq.heappush(self.max, -num)  
        
        if len(self.max) - len(self.min) > 1:
            val = heapq.heappop(self.max)
            heapq.heappush(self.min, -val)
        elif len(self.min) - len(self.max) > 1:
            val = heapq.heappop(self.min)
            heapq.heappush(self.max, -val)
        
    def findMedian(self) -> float:
        if len(self.max) > len(self.min):
            return -self.max[0]
        elif len(self.min) > len(self.max):
            return self.min[0]
        else:
            return ((self.min[0] - self.max[0]) / 2)

        
        