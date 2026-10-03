import heapq

class MedianFinder:
    def __init__(self):
        # Stores the smaller half of the numbers (Max-Heap using negatives)
        self.small = []
        # Stores the larger half of the numbers (Min-Heap using positives)
        self.large = []

    def addNum(self, num: int) -> None:
        # Step 1: Push to small (max-heap) first.
        heapq.heappush(self.small, -num)
        
        # Step 2: Every time we push to small, we must pass its largest element 
        # over to large to ensure all elements in 'large' are strictly greater.
        val = -heapq.heappop(self.small)
        heapq.heappush(self.large, val)
        
        # Step 3: Enforce the balance rule. 
        # 'small' is allowed to be exactly 1 element bigger than 'large' (for odd lengths).
        # 'large' is NEVER allowed to be bigger than 'small'.
        if len(self.large) > len(self.small):
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -val)

    def findMedian(self) -> float:
        # If lengths are equal, total count is even. Average the two middle values.
        if len(self.small) == len(self.large):
            return (-self.small[0] + self.large[0]) / 2.0
            
        # If lengths are different, 'small' holds the extra element. It is the median.
        return float(-self.small[0])