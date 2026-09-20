class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
            
        m, n = len(nums1), len(nums2)
        left, right = 0, m
        half_len = (m + n + 1) // 2
        
        while left <= right:
            i = (left + right) // 2
            j = half_len - i
            
            # Use 1,000,001 as "infinity" to avoid slow float object creation
            max_A = nums1[i-1] if i > 0 else -1000001
            min_A = nums1[i] if i < m else 1000001
            max_B = nums2[j-1] if j > 0 else -1000001
            min_B = nums2[j] if j < n else 1000001
            
            if max_A <= min_B and max_B <= min_A:
                if (m + n) % 2 == 1:
                    return float(max(max_A, max_B))
                return (max(max_A, max_B) + min(min_A, min_B)) / 2.0
                
            elif max_A > min_B:
                right = i - 1
            else:
                left = i + 1