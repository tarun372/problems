class Solution:
    def findMedianSortedArrays(self, A: list[int], B: list[int]) -> float:
        if len(A) > len(B): 
            A, B = B, A
            
        m, n = len(A), len(B)
        left, right = 0, m
        
        while left <= right:
            i = (left + right) // 2
            j = (m + n + 1) // 2 - i
            
            # Condense the boundary checks
            max_A = A[i-1] if i > 0 else float('-inf')
            min_A = A[i] if i < m else float('inf')
            max_B = B[j-1] if j > 0 else float('-inf')
            min_B = B[j] if j < n else float('inf')
            
            # The Cross-Check
            if max_A <= min_B and max_B <= min_A:
                if (m + n) % 2 == 0:
                    return (max(max_A, max_B) + min(min_A, min_B)) / 2.0
                return float(max(max_A, max_B))
                
            # Move Partitions
            if max_A > min_B:
                right = i - 1
            else:
                left = i + 1