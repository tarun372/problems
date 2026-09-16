class Solution:
    def minDays(self, bloomDay: list[int], m: int, k: int) -> int:
        # Edge Case: If we need more total flowers than exist in the garden, it's impossible.
        if m * k > len(bloomDay):
            return -1
            
        # 1. Define the Search Space
        low = min(bloomDay)
        high = max(bloomDay)
        
        while low < high:
            mid = low + (high - low) // 2
            
            # 2. THE MAGIC CONDITION: Can we make 'm' bouquets on day 'mid'?
            bouquets_made = 0
            adjacent_flowers = 0
            
            for day in bloomDay:
                # Is this flower blooming on or before our test day?
                if day <= mid:
                    adjacent_flowers += 1
                    # Did we collect enough adjacent flowers for a bouquet?
                    if adjacent_flowers == k:
                        bouquets_made += 1
                        adjacent_flowers = 0 # Reset for the next bouquet
                else:
                    # The streak is broken by an unbloomed flower. Reset the count.
                    adjacent_flowers = 0
                    
            # 3. Update Boundaries
            if bouquets_made >= m:
                # True! We made enough. Can we do it in fewer days?
                high = mid
            else:
                # False! We didn't make enough. We must wait more days.
                low = mid + 1
                
        # low and high converge on the minimum valid day
        return low