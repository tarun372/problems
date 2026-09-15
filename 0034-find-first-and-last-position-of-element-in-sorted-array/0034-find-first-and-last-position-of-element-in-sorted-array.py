class Solution(object):
    def searchRange(self, nums, target):
        def find_bound(is_first):
            ans = -1
            low = 0
            high = len(nums) - 1
            
            while low <= high:
                # Good habit: prevents integer overflow in other languages
                mid = low + (high - low) // 2 
                
                if nums[mid] == target:
                    ans = mid
                    if is_first:
                        high = mid - 1  # Keep looking left
                    else:
                        low = mid + 1   # Keep looking right
                        
                elif nums[mid] > target:
                    high = mid - 1
                else:
                    low = mid + 1
                    
            return ans

        # Call the same function, just flip the flag
        first_pos = find_bound(is_first=True)
        
        # Early exit: if the first position isn't found, the target isn't in the array
        if first_pos == -1:
            return [-1, -1]
            
        last_pos = find_bound(is_first=False)
        
        return [first_pos, last_pos]