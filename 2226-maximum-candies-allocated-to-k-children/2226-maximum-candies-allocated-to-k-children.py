class Solution:
    def maximumCandies(self, candies: list[int], k: int) -> int:
        # STEP 0: The Edge Case
        # If the total candies in the world are less than k, 
        # it's impossible to even give 1 candy to each child.
        if sum(candies) < k:
            return 0
            
        # STEP 1: Set the Search Space
        low = 1
        high = max(candies)
        best_candy_count = 0
        
        # STEP 2: The Binary Search Loop
        while low <= high:
            mid = low + (high - low) // 2
            
            # --- THE SIMULATION ---
            children_fed = 0
            for pile in candies:
                # Floor division (//) enforces the "cannot merge piles" rule.
                # If a pile has 10 candies, and mid is 4: 10 // 4 = 2 portions.
                # The remaining 2 candies are ignored.
                children_fed += pile // mid
            # ----------------------
            
            # STEP 3: React to the Result
            if children_fed >= k:
                # True! We successfully created enough portions for 'k' children.
                # Record this success, but try to MAXIMIZE the candies.
                best_candy_count = mid
                low = mid + 1  # Search for a bigger portion size
            else:
                # False! We didn't make enough portions for all 'k' children.
                # We were too greedy. We must shrink the portion size.
                high = mid - 1
                
        return best_candy_count