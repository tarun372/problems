class Solution:
    def hIndex(self, citations: list[int]) -> int:
        n = len(citations)
        low = 0
        high = n - 1
        
        while low <= high:
            mid = low + (high - low) // 2
            
            # Count of papers from 'mid' to the end of the array
            count = n - mid
            
            # THE MAGIC CONDITION
            if citations[mid] == count:
                # Perfect match! Because the array is sorted, this is the optimal h-index.
                return count
                
            elif citations[mid] > count:
                # True! This is a valid h-index.
                # But we want to maximize the 'count', so we need to look for a smaller index (to the left)
                high = mid - 1
                
            else:
                # False! The citations are too low to support this 'count'.
                # We must move to the right to find papers with more citations.
                low = mid + 1
                
        # If there's no exact match, 'low' will settle on the first valid index.
        # The h-index is the count of papers from 'low' to the end.
        return n - low