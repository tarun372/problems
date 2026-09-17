class Solution:
    def shipWithinDays(self, weights: list[int], days: int) -> int:
        low = max(weights)
        high = sum(weights)
        
        while low < high:
            mid = (low + high) // 2
            
            days_needed = 1
            curr_weight = 0
            
            for w in weights:
                # If adding this weight overflows, reset for a new day
                if curr_weight + w > mid:
                    days_needed += 1
                    curr_weight = 0  
                
                # Add the weight (happens every single loop, no 'else' needed)
                curr_weight += w
                
            if days_needed > days:
                low = mid + 1
            else:
                high = mid
                
        return low