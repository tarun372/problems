class Solution:
    def kthSmallest(self, matrix: list[list[int]], k: int) -> int:
        n = len(matrix)
        
        # 1. Set the boundaries based on the smallest and largest actual values
        left = matrix[0][0]
        right = matrix[n-1][n-1]
        
        while left < right:
            mid = left + (right - left) // 2
            
            # --- THE VALIDATOR ---
            # Start at the bottom-left corner to count numbers <= mid
            count = 0
            row = n - 1
            col = 0
            
            while row >= 0 and col < n:
                if matrix[row][col] <= mid:
                    # If this bottom number is <= mid, everything ABOVE it is too!
                    # Add this entire chunk of the column to our count.
                    count += (row + 1)
                    # Move right to check the next column
                    col += 1
                else:
                    # This number is too big. Move up to a smaller number.
                    row -= 1
            # ----------------------
            
            # 3. React to the Result
            if count < k:
                # We didn't find enough small numbers. Our guess was too low.
                left = mid + 1
            else:
                # We found k or more! This means 'mid' is a potential answer,
                # but let's try to squeeze it even smaller.
                right = mid
                
        return left