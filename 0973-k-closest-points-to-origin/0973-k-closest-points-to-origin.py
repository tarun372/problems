import random

class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        # Helper function to get the squared distance (avoids slow square roots)
        def get_dist(i):
            return points[i][0]**2 + points[i][1]**2

        # Partitions the array around a pivot
        def partition(left, right, pivot_idx):
            pivot_dist = get_dist(pivot_idx)
            
            # Move pivot out of the way to the end
            points[pivot_idx], points[right] = points[right], points[pivot_idx]
            
            store_idx = left
            for i in range(left, right):
                # If the point is closer than the pivot, toss it to the left side
                if get_dist(i) < pivot_dist:
                    points[store_idx], points[i] = points[i], points[store_idx]
                    store_idx += 1
                    
            # Move the pivot to its final, correct sorted position
            points[store_idx], points[right] = points[right], points[store_idx]
            return store_idx

        def quickselect(left, right):
            if left >= right:
                return
                
            # Pick a random pivot to avoid worst-case O(N^2) on sorted arrays
            pivot_idx = random.randint(left, right)
            
            # Partition the array and get the pivot's true index
            true_idx = partition(left, right, pivot_idx)
            
            # If the pivot landed exactly at k, the left side has our k closest points!
            if true_idx == k:
                return
            # If the pivot landed too far right, search the left half
            elif true_idx > k:
                quickselect(left, true_idx - 1)
            # If the pivot landed too far left, search the right half
            else:
                quickselect(true_idx + 1, right)

        # Start the quickselect process on the full array
        quickselect(0, len(points) - 1)
        
        # The first k elements are now the closest ones (though not perfectly sorted among themselves)
        return points[:k]