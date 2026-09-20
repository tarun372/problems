class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
            
        m = len(matrix)       # Number of rows
        n = len(matrix[0])    # Number of columns
        
        # Pretend the matrix is a 1D array
        left = 0
        right = m * n - 1 
        
        while left <= right:
            mid = left + (right - left) // 2
            
            # --- THE MAGIC TRANSLATION ---
            # Translate the 1D 'mid' index back into a 2D grid coordinate
            row = mid // n
            col = mid % n
            
            mid_value = matrix[row][col]
            # -----------------------------
            
            if mid_value == target:
                return True
            elif mid_value < target:
                left = mid + 1
            else:
                right = mid - 1
                
        return False