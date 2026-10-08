class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
            
        a, b = 0, 1
        
        # Slide a window of size 2 up to n
        for _ in range(2, n + 1):
            # Calculate the next number, and shift the variables forward
            a, b = b, a + b
            
        return b