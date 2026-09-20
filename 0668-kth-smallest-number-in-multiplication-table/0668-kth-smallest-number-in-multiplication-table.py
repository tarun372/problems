class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        # HACK 1: Always loop over the smaller dimension
        if m > n:
            m, n = n, m
            
        left = 1
        right = m * n
        
        while left < right:
            mid = (left + right) // 2
            
            count = 0
            # Inline simulation for maximum speed
            for i in range(1, m + 1):
                val = mid // i
                
                # HACK 2: Early Exit
                if val == 0:
                    break
                    
                # HACK 3: No function calls
                if val > n:
                    count += n
                else:
                    count += val
                    
            if count < k:
                left = mid + 1
            else:
                right = mid
                
        return left