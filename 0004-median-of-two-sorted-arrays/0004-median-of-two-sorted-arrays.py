class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        # SPEED HACK: Always binary search the smaller array.
        # This guarantees our time complexity is O(log(min(m, n)))
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
            
        m, n = len(nums1), len(nums2)
        
        # We search for the perfect partition index in nums1
        left = 0
        right = m
        
        # The total number of elements that MUST be in the left half of the merged array
        half_len = (m + n + 1) // 2
        
        while left <= right:
            partition1 = (left + right) // 2
            
            # If we take 'partition1' elements from nums1, we MUST take the rest from nums2
            partition2 = half_len - partition1
            
            # Find the 4 boundary numbers touching our dividing lines
            # Use negative/positive infinity if a partition is at the extreme edge
            maxLeft1 = float('-inf') if partition1 == 0 else nums1[partition1 - 1]
            minRight1 = float('inf') if partition1 == m else nums1[partition1]
            
            maxLeft2 = float('-inf') if partition2 == 0 else nums2[partition2 - 1]
            minRight2 = float('inf') if partition2 == n else nums2[partition2]
            
            # --- THE VALIDATOR ---
            # Did we find the perfect split?
            if maxLeft1 <= minRight2 and maxLeft2 <= minRight1:
                
                # If total length is even, median is average of the two middle numbers
                if (m + n) % 2 == 0:
                    return (max(maxLeft1, maxLeft2) + min(minRight1, minRight2)) / 2.0
                
                # If total length is odd, median is just the largest number on the left
                else:
                    return float(max(maxLeft1, maxLeft2))
                    
            # We took too many numbers from nums1. Move the partition left.
            elif maxLeft1 > minRight2:
                right = partition1 - 1
                
            # We didn't take enough numbers from nums1. Move the partition right.
            else:
                left = partition1 + 1