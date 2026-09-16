class Solution:
    def maximumCandies(self, candies: list[int], k: int) -> int:
        
        # SPEED HACK 1: Tighter 'high' bound.
        # The mathematical absolute maximum candy a child could get.
        high = sum(candies) // k
        
        # If this is 0, it means we don't even have enough total candy for 1 each.
        if high == 0:
            return 0
            
        low = 1
        best_candy_count = 0
        
        while low <= high:
            mid = low + (high - low) // 2
            
            children_fed = 0
            for pile in candies:
                children_fed += pile // mid
                
                # SPEED HACK 2: The Early Exit
                # We hit our goal! Stop looping through the rest of the array immediately.
                if children_fed >= k:
                    break
                    
            if children_fed >= k:
                best_candy_count = mid
                low = mid + 1
            else:
                high = mid - 1
                
        return best_candy_count