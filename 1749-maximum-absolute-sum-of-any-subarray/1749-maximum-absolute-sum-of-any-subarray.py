class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        max_sum = 0
        min_sum = 0
        current_max = 0
        current_min = 0
        
        for n in nums:
            # Track the maximum positive sum
            current_max = max(0, current_max + n)
            max_sum = max(max_sum, current_max)
            
            # Track the minimum negative sum
            current_min = min(0, current_min + n)
            min_sum = min(min_sum, current_min)
            
        # Convert the negative result to positive right at the end!
        return max(max_sum, abs(min_sum))