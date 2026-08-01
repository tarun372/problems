class Solution:
    def isHappy(self, n: int) -> bool:
        # Helper function to calculate the sum of the squares of digits
        def get_next(number):
            total_sum = 0
            while number > 0:
                number, digit = divmod(number, 10)
                total_sum += digit ** 2
            return total_sum
        
        # Initialize the slow and fast pointers
        slow = n
        fast = get_next(n) # Fast starts one step ahead
        
        # Loop until fast reaches 1 (happy) or fast catches slow (cycle)
        while fast != 1 and slow != fast:
            slow = get_next(slow)                  # Moves 1 step
            fast = get_next(get_next(fast))        # Moves 2 steps
            
        # If the loop stopped because fast hit 1, it is a happy number
        return fast == 1