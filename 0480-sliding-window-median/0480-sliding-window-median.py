import heapq
from collections import defaultdict

class Solution:
    def medianSlidingWindow(self, nums: list[int], k: int) -> list[float]:
        small = []  # Max-Heap (stores smaller half, inverted)
        large = []  # Min-Heap (stores larger half)
        deleted = defaultdict(int)  # The graveyard for numbers outside the window
        res = []
        
        # 1. Initialize the first window (Standard Two Heaps logic)
        for i in range(k):
            heapq.heappush(small, -nums[i])
            heapq.heappush(large, -heapq.heappop(small))
            if len(large) > len(small):
                heapq.heappush(small, -heapq.heappop(large))
                
        def get_median():
            if k % 2 == 1:
                return float(-small[0])
            return (-small[0] + large[0]) / 2.0
            
        res.append(get_median())
        
        # 2. Slide the window
        for i in range(k, len(nums)):
            in_num = nums[i]
            out_num = nums[i - k]
            
            # Step A: Mark the outgoing number as a ghost in the graveyard
            deleted[out_num] += 1
            
            # Step B: Balance tracking
            # We use a 'balance' integer to track the ACTIVE sizes of our heaps.
            # If the outgoing ghost is in 'small', 'small' effectively loses 1 active element (balance = -1).
            # If the outgoing ghost is in 'large', 'large' effectively loses 1 active element (balance = +1).
            balance = -1 if out_num <= -small[0] else 1
            
            # Step C: Add the new incoming number
            if small and in_num <= -small[0]:
                balance += 1
                heapq.heappush(small, -in_num)
            else:
                balance -= 1
                heapq.heappush(large, in_num)
                
            # Step D: Rebalance active elements
            # If balance < 0, small needs an element from large.
            # If balance > 0, large needs an element from small.
            if balance < 0:
                heapq.heappush(small, -heapq.heappop(large))
            elif balance > 0:
                heapq.heappush(large, -heapq.heappop(small))
                
            # Step E: Lazy Deletion (The most important step!)
            # Check the tops of both heaps. If the number at the top is a ghost in our graveyard,
            # we finally pop it permanently and decrement its graveyard count.
            # We use a while loop because there might be multiple ghosts stacked at the top!
            while small and deleted[-small[0]] > 0:
                deleted[-small[0]] -= 1
                heapq.heappop(small)
                
            while large and deleted[large[0]] > 0:
                deleted[large[0]] -= 1
                heapq.heappop(large)
                
            # Now that the tops are guaranteed to be real, active elements, grab the median.
            res.append(get_median())
            
        return res