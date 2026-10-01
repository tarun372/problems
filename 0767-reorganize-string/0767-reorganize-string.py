import heapq
from collections import Counter

class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)
        # Build Max-Heap format: [-frequency, character]
        max_heap = [[-cnt, char] for char, cnt in count.items()]
        heapq.heapify(max_heap)
        
        prev = None  # Acts as our cooldown waiting room
        res = []
        
        while max_heap or prev:
            # If the heap is empty but we still have a character waiting to be placed,
            # we are forced to place it back-to-back. It's impossible!
            if not max_heap and prev:
                return ""
            
            # 1. Grab the most frequent available character
            cnt, char = heapq.heappop(max_heap)
            res.append(char)
            cnt += 1  # It's negative, so adding 1 reduces its remaining count
            
            # 2. Release the previous character from the waiting room back into the heap
            if prev:
                heapq.heappush(max_heap, prev)
                prev = None
                
            # 3. If our current character still needs to be placed, put it in the waiting room
            if cnt != 0:
                prev = [cnt, char]
                
        return "".join(res)