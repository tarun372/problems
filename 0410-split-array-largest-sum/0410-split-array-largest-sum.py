class Solution:
    def splitArray(self, nums: list[int], k: int) -> int:
        # The lowest possible max sum is the largest single element 
        # (you can't split a single element).
        left = max(nums)
        # The highest possible max sum is if k=1 and one subarray gets everything.
        right = sum(nums)
        
        while left < right:
            mid = left + (right - left) // 2
            
            # --- THE SIMULATION ---
            # How many subarrays do we need if the max sum is 'mid'?
            subarrays_needed = 1
            current_sum = 0
            
            for num in nums:
                if current_sum + num > mid:
                    # We hit the limit! Start a new subarray.
                    subarrays_needed += 1
                    current_sum = num
                else:
                    # Keep adding to the current subarray.
                    current_sum += num
            # ----------------------
            
            # React to the Result
            if subarrays_needed > k:
                # We used too many subarrays. The 'mid' limit was too small.
                left = mid + 1
            else:
                # We successfully split it in 'k' (or fewer) subarrays!
                # Let's try to squeeze the maximum sum even lower.
                right = mid
                
        return left