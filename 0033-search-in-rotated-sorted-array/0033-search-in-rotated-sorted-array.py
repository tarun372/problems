class Solution:
    def search(self, nums: list[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        
        while low <= high:
            mid = low + (high - low) // 2
            
            # Did we find it?
            if nums[mid] == target:
                return mid
                
            # THE MAGIC CONDITION: Which half is sorted?
            
            # Case 1: The LEFT half is perfectly sorted
            if nums[low] <= nums[mid]: 
                # Is our target mathematically inside this left half?
                if nums[low] <= target < nums[mid]:
                    high = mid - 1  # Yes! Discard the right half.
                else:
                    low = mid + 1   # No! Discard the left half.
                    
            # Case 2: The RIGHT half is perfectly sorted
            else:
                # Is our target mathematically inside this right half?
                if nums[mid] < target <= nums[high]:
                    low = mid + 1   # Yes! Discard the left half.
                else:
                    high = mid - 1  # No! Discard the right half.
                    
        return -1 # Target is not in the array