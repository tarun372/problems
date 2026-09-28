import heapq

class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        # 1. Convert to a Max-Heap by making all weights negative
        max_heap = [-s for s in stones]
        heapq.heapify(max_heap)
        
        # 2. Keep smashing until 1 or 0 stones remain
        while len(max_heap) > 1:
            # Pop the two heaviest stones. 
            # (Because they are negative, the "heaviest" is mathematically the smallest)
            stone1 = heapq.heappop(max_heap) # e.g., -8
            stone2 = heapq.heappop(max_heap) # e.g., -7
            
            # If they are equal, they both destroy each other (do nothing).
            # If they are different, push the difference back into the heap.
            if stone1 != stone2:
                # The math works perfectly with negatives: -8 - (-7) = -1
                heapq.heappush(max_heap, stone1 - stone2)
                
        # 3. If a stone is left, flip its sign back. If the heap is empty, return 0.
        return -max_heap[0] if max_heap else 0