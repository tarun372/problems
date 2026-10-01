import heapq

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: list[int], capital: list[int]) -> int:
        # 1. Zip the arrays together and sort by capital required (ascending)
        # Format: (capital_required, profit)
        projects = sorted(zip(capital, profits))
        
        max_heap = []
        ptr = 0
        n = len(projects)
        
        # 2. We can only execute a maximum of k projects
        for _ in range(k):
            
            # 3. Unlock phase: Add all currently affordable projects to our Max-Heap
            while ptr < n and projects[ptr][0] <= w:
                # Push the profit (negative to simulate a Max-Heap in Python)
                heapq.heappush(max_heap, -projects[ptr][1])
                ptr += 1
                
            # 4. If the heap is empty, we can't afford any remaining projects. Stop early.
            if not max_heap:
                break
                
            # 5. Execute phase: Pop the most profitable project and add it to our capital
            w += -heapq.heappop(max_heap)
            
        return w