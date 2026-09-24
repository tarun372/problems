class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        
        distance = [point[0]**2 + point[1]**2 for point in points]
        hp = distance.copy()
        heapq.heapify(hp)

        for i in range(k):
            thresh = heapq.heappop(hp)

        res = []
        for i in range(len(distance)):
            if distance[i] <= thresh:
                res.append(points[i])
        
        return res