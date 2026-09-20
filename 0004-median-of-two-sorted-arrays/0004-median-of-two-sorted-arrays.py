class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        # 1. Always binary search the smaller array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
            
        m, n = len(nums1), len(nums2)
        
        # 2. Early Exit: If one array is empty, calculate median instantly
        # This completely skips the while loop overhead for common test cases.
        if m == 0:
            mid = n >> 1
            if n % 2 == 1:
                return float(nums2[mid])
            return (nums2[mid - 1] + nums2[mid]) / 2.0

        left, right = 0, m
        # Bitwise shift (>> 1) is slightly faster than floor division (// 2)
        half_len = (m + n + 1) >> 1 
        
        while left <= right:
            i = (left + right) >> 1
            j = half_len - i
            
            max_A = nums1[i-1] if i > 0 else -1000001
            min_A = nums1[i] if i < m else 1000001
            max_B = nums2[j-1] if j > 0 else -1000001
            min_B = nums2[j] if j < n else 1000001
            
            if max_A <= min_B and max_B <= min_A:
                
                # 3. Kill the max() function. Inline it for raw speed.
                left_max = max_A if max_A > max_B else max_B
                
                if (m + n) % 2 == 1:
                    return float(left_max)
                    
                # 4. Kill the min() function. Inline it for raw speed.
                right_min = min_A if min_A < min_B else min_B
                return (left_max + right_min) / 2.0
                
            elif max_A > min_B:
                right = i - 1
            else:
                left = i + 1