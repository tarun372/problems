class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        start = 0
        end = len(nums) - 1
        
        while start < end:
            mid = start + (end - start) // 2
            
            # If the right neighbor is greater, there MUST be a peak to the right
            if nums[mid] < nums[mid + 1]:
                start = mid + 1
                
            # If the right neighbor is smaller, there MUST be a peak to the left (or at mid)
            else:
                end = mid
                
        return start