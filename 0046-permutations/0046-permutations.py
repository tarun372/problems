class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        res = []
        
        # We track our progress using an index called 'start'
        def backtrack(start):
            # 1. Base Case: If the start pointer reaches the end, we have a full permutation
            if start == len(nums):
                # Critical: We must append a COPY of the array, not the reference!
                res.append(nums[:])
                return
            
            # 2. Iterate through all available choices for the current position
            for i in range(start, len(nums)):
                
                # CHOOSE: Swap the current element with the 'start' element
                nums[start], nums[i] = nums[i], nums[start]
                
                # EXPLORE: Move the start pointer forward by 1
                backtrack(start + 1)
                
                # UN-CHOOSE (Backtrack): Swap them back to restore the original array
                nums[start], nums[i] = nums[i], nums[start]
                
        # Kick off the recursion with the pointer at index 0
        backtrack(0)
        return res