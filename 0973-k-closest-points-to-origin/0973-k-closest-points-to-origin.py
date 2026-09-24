import heapq
from typing import List

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        min_heap = []

        for point in points:
            dist = self.calc_distance(point[0], point[1])
            heapq.heappush(min_heap, (dist, point))

        ans = []
        for _ in range(k):
            _, point = heapq.heappop(min_heap)
            ans.append(point)

        return ans

    def calc_distance(self, x: int, y: int) -> int:
        return x * x + y * y