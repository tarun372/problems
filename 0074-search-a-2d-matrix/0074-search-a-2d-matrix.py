class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        n = len(matrix[0]) # We only keep 'n' because we divide by it frequently
        left, right = 0, (len(matrix) * n) - 1 
        
        while left <= right:
            mid = (left + right) // 2
            
            # Look up the matrix value directly without storing it in a variable
            if matrix[mid // n][mid % n] == target:
                return True
            elif matrix[mid // n][mid % n] < target:
                left = mid + 1
            else:
                right = mid - 1
                
        return False