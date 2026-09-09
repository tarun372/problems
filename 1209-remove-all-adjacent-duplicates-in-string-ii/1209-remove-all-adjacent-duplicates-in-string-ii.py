class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        # Initialize an Empty Stack to keep track of characters and their counts.
        stack = []
        
        # Iterate Through the Input String
        for i in s:
            # Check for Duplicates in Stack
            if stack and i == stack[-1][0]:
                # If duplicate found, update the count in the stack
                stack[-1][1] += 1
                
                # Check if Count Exceeds 'k', pop the character if necessary
                if stack[-1][1] >= k:
                    stack.pop()
            else:
                # Handle Non-Duplicate Characters
                # If current character is not equal to the top character in the stack, or the stack is empty,
                # append a new pair [i, 1] onto the stack.
                stack.append([i, 1])
        
        # Construct Result String
        res = ""
        for char, n in stack:
            # After processing all characters, construct the result string by repeating each character according to its count.
            res += char * n
        
        # Return the Final Result
        return res