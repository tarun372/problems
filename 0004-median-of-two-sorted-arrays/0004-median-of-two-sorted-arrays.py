class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        # 1. Combine and sort the arrays purely in C
        merged = sorted(nums1 + nums2)
        total = len(merged)
        
        # 2. Find the median directly
        mid = total // 2
        
        if total % 2 == 0:
            return (merged[mid - 1] + merged[mid]) / 2.0
        else:
            return float(merged[mid])