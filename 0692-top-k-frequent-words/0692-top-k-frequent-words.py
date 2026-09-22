import heapq
from collections import Counter

class Solution:
    def topKFrequent(self, words: list[str], k: int) -> list[str]:
        # 1. Count frequencies
        count = Counter(words)
        
        # 2. Build the heap array in one go.
        # -freq: Most frequent words become the most negative (rise to top)
        # word: Alphabetically smaller words naturally rise to top on ties
        heap = [(-freq, word) for word, freq in count.items()]
        
        # 3. Transform the list into a heap in O(N) time
        heapq.heapify(heap)
        
        # 4. Pop the top K elements. They are perfectly sorted!
        return [heapq.heappop(heap)[1] for _ in range(k)]