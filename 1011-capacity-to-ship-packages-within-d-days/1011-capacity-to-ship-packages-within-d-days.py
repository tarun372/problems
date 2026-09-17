class Solution:
    def shipWithinDays(self, weights: list[int], days: int) -> int:
        
        # Helper function so we can use "return False" for an instant Early Exit
        def can_ship(capacity):
            days_needed = 1
            current_weight = 0
            
            for weight in weights:
                if current_weight + weight > capacity:
                    days_needed += 1
                    current_weight = weight
                    
                    # SPEED HACK: The Early Exit
                    # If we just exceeded our allowed days, stop immediately!
                    if days_needed > days:
                        return False 
                else:
                    current_weight += weight
                    
            return True

        # 1. Set the Search Space
        low = max(weights)
        high = sum(weights)
        
        # 2. The Binary Search Loop
        while low < high:
            mid = low + (high - low) // 2
            
            if can_ship(mid):
                # True! This capacity works. 
                # Let's try to find an even smaller one.
                # Notice we use 'high = mid' here (no infinite loop risk on "Minimize" problems!)
                high = mid 
            else:
                # False! The ship was too small (Early Exit triggered).
                low = mid + 1
                
        return low