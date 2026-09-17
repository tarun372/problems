class Solution:
    def shipWithinDays(self, weights: list[int], days: int) -> int:
        
        # 1. Set the Search Space
        low = max(weights)   # Ship must hold at least the heaviest single package
        high = sum(weights)  # Ship could theoretically hold everything at once
        best_capacity = -1
        
        # 2. The Binary Search Loop
        while low <= high:
            mid = low + (high - low) // 2
            
            # --- THE SIMULATION ---
            # Pretend our ship's capacity is 'mid'. How many days will it take?
            days_needed = 1
            current_weight = 0
            
            for weight in weights:
                # If adding this package sinks the ship...
                if current_weight + weight > mid:
                    # ...send the ship away. Wait for tomorrow!
                    days_needed += 1
                    current_weight = weight # Put the package on tomorrow's ship
                else:
                    # Otherwise, just load it onto today's ship
                    current_weight += weight
            # ----------------------
            
            # 3. React to the Result
            if days_needed <= days:
                # True! We shipped everything in time.
                # Record this as a valid answer, but try to find an EVEN SMALLER ship.
                best_capacity = mid
                high = mid - 1
            else:
                # False! We took too many days. The ship is too tiny!
                # We must build a bigger ship.
                low = mid + 1
                
        return best_capacity