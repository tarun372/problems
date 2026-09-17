class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        n = len(weights)

        max_weight = max(weights)
        max_packages_per_day = math.ceil(n / days)
        max_capacity = max_packages_per_day * max_weight
        min_capacity = max(max_weight, math.floor(sum(weights) / days))

        # capacities = list(range(min_capacity, max_capacity + 1))

        # apply binary search to capacities list to
        # find which is the least 
        left = min_capacity
        right = max_capacity
        
        while left < right:
            middle = left + (right - left) // 2
            
            if self._is_capacity_enough(middle, weights, days):
                right = middle
            else:
                left = middle + 1
        
        return left
    
    def _is_capacity_enough(
        self,
        capacity: int,
        weights: list[int],
        days: int,
    ) -> bool:
        used_days = 1
        used_capacity = 0
        for weight in weights:
            used_capacity += weight
            if used_capacity > capacity:
                used_days += 1
                used_capacity = weight
        return used_days <= days