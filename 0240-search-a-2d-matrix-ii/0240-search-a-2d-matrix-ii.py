class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
            
        # Start at the top-right corner
        row = 0
        col = len(matrix[0]) - 1
        
        # Keep searching as long as we haven't fallen off the grid
        while row < len(matrix) and col >= 0:
            current = matrix[row][col]
            
            if current == target:
                return True
                
            elif current > target:
                # The current number is too big. 
                # Since everything below it is even bigger, we can eliminate this entire column.
                col -= 1
                
            else:
                # The current number is too small.
                # Since everything to the left is even smaller, we can eliminate this entire row.
                row += 1
                
        # We fell off the grid without finding the target
        return False