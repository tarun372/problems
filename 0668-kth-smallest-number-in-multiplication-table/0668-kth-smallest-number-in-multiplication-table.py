class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        # 1. Set the boundaries (1 to max possible value)
        left = 1
        right = m * n
        
        while left < right:
            mid = left + (right - left) // 2
            
            # --- THE VALIDATOR ---
            count = 0
            # Check every row from 1 up to 'm'
            for i in range(1, m + 1):
                # Count how many multiples of 'i' are <= mid.
                # It caps out at 'n' (the end of the row).
                count += min(mid // i, n)
            # ----------------------
            
            # 3. React to the Result
            if count < k:
                # We didn't find enough small numbers. Guess higher.
                left = mid + 1
            else:
                # We found k or more! 'mid' is a potential answer.
                # Squeeze the upper bound down to find the exact first occurrence.
                right = mid
                
        return left