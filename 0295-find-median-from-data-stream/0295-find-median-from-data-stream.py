import heapq
class MedianFinder:

    def __init__(self):
        self.max_heap = []
        self.min_heap = []
        heapq.heapify(self.max_heap)
        heapq.heapify(self.min_heap)
    def addNum(self, num: int) -> None:
        if(not self.max_heap and not self.min_heap):
            heapq.heappush(self.max_heap , -num)
        else:
            if(len(self.max_heap) == len(self.min_heap)):
                if(num <= -self.max_heap[0]):
                    heapq.heappush(self.max_heap , -num)
                else:
                    heapq.heappush(self.min_heap , num)
                    heapq.heappush(self.max_heap , -heapq.heappop(self.min_heap))
            else:
                if(num <= -self.max_heap[0]):
                    heapq.heappush(self.max_heap , -num)
                    heapq.heappush(self.min_heap , -heapq.heappop(self.max_heap))
                else:
                    heapq.heappush(self.min_heap , num)
    def findMedian(self) -> float:
        if(not self.max_heap):
            return None
        if(len(self.max_heap) == len(self.min_heap)):
            return (-(self.max_heap[0]) + (self.min_heap[0]))/ 2
        else:
            return -self.max_heap[0]

        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()