import math

class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        # Minimum possible speed: 1 banana per hour
        low = 1
        
        # Maximum possible speed: eating the biggest pile in 1 hour
        high = max(piles)
        
        while low < high:
            mid = low + (high - low) // 2
            
            # THE MAGIC CONDITION: Can Koko finish all bananas at 'mid' speed?
            hours_needed = 0
            for pile in piles:
                # If pile is 7 and speed is 3, it takes ceil(7/3) = 3 hours
                hours_needed += math.ceil(pile / mid)
                
            if hours_needed <= h:
                # True! She can finish in time. 
                # But can she eat even slower? Let's check the left side.
                high = mid
            else:
                # False! She took too long. 
                # She must eat faster. Let's check the right side.
                low = mid + 1
                
        # low and high converge on the absolute minimum valid speed
        return low