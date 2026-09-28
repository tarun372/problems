import heapq

class Solution:
    def kWeakestRows(self, mat: list[list[int]], k: int) -> list[int]:
        # Helper function to binary search the count of 1s in a sorted row
        def count_soldiers(row):
            left, right = 0, len(row)
            while left < right:
                mid = (left + right) // 2
                if row[mid] == 1:
                    # We are on a soldier. The boundary must be to the right.
                    left = mid + 1
                else:
                    # We are on a civilian. The boundary is here or to the left.
                    right = mid
            # The left pointer lands exactly on the count of 1s
            return left
        
        # Build a list of tuples: (soldier_count, row_index)
        row_strengths = [(count_soldiers(mat[i]), i) for i in range(len(mat))]
        
        # Transform the list into a Min-Heap based on the tuples
        heapq.heapify(row_strengths)
        
        # Pop the k weakest rows. 
        # Python naturally breaks ties by comparing the second item in the tuple (the index!)
        return [heapq.heappop(row_strengths)[1] for _ in range(k)]