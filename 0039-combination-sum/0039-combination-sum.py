class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        res = []
        path = []
        
        # We track 'start_index' to avoid duplicate combinations like [2,3] and [3,2]
        def backtrack(start_index, current_sum):
            
            # 1. Base Case: We hit the exact target!
            if current_sum == target:
                res.append(path[:])  # Deep copy the valid path
                return
                
            # 2. Base Case: We overshot the target (Pruning)
            if current_sum > target:
                return
                
            # 3. Explore from the 'start_index' to the end of the array
            for i in range(start_index, len(candidates)):
                
                # CHOOSE
                path.append(candidates[i])
                
                # EXPLORE
                # Notice we pass 'i' instead of 'i + 1'. 
                # This is the "Unlimited Supply" trick! It lets us reuse candidates[i].
                backtrack(i, current_sum + candidates[i])
                
                # UN-CHOOSE (Backtrack)
                path.pop()
                
        # Kick off the recursion starting at index 0 with a sum of 0
        backtrack(0, 0)
        return res