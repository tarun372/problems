import heapq
import math


class Solution:
    def kClosest(
        self,
        points: list[list[int]],
        k: int,
    ) -> list[list[int]]:
        points_dist = []
        heapq.heapify(points_dist)

        for i in range(len(points)):
            dist = math.sqrt(
                (0 - points[i][0]) ** 2
                + (0 - points[i][1]) ** 2
            )
            heapq.heappush(points_dist, (dist, points[i]))

        res = []

        for _ in range(k):
            val = heapq.heappop(points_dist)
            res.append(val[1])

        return res