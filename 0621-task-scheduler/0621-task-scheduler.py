import heapq
from collections import Counter, deque

class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        # 1. Count frequencies and build a Max-Heap
        count = Counter(tasks)
        max_heap = [-cnt for cnt in count.values()]
        heapq.heapify(max_heap)
        
        time = 0
        # The waiting room queue. Will store pairs: [remaining_frequency, time_it_unlocks]
        q = deque()
        
        # 2. Simulate the CPU cycles
        while max_heap or q:
            time += 1
            
            # If we have available tasks, execute the most frequent one
            if max_heap:
                # Pop the most frequent task
                cnt = heapq.heappop(max_heap)
                cnt += 1 # It's negative, so adding 1 reduces its remaining count
                
                # If the task still needs to run again, put it in the waiting room
                if cnt != 0:
                    q.append([cnt, time + n])
            
            # Check if the task at the front of the waiting room is ready to be unlocked
            if q and q[0][1] == time:
                # Take it out of the queue and put it back into the heap
                unlocked_task = q.popleft()[0]
                heapq.heappush(max_heap, unlocked_task)
                
        return time