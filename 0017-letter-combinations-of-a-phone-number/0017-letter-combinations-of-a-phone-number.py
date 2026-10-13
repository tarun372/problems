class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        # Edge case: If the input is empty, return an empty list immediately
        if not digits:
            return []
            
        # 1. Create a dictionary to map each digit to its corresponding letters
        phone_map = {
            '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
            '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
        }
        
        res = []
        
        # 2. Define the backtracking function
        def backtrack(index, current_str):
            
            # Base Case: If our string length matches the number of digits, we're done
            if index == len(digits):
                res.append(current_str)
                return
                
            # Find all possible letters for the current digit
            current_digit = digits[index]
            possible_letters = phone_map[current_digit]
            
            # 3. Choose, Explore, Un-choose
            for letter in possible_letters:
                # Because strings are immutable, current_str + letter creates a 
                # new string for the next branch. The "Un-choose" happens 
                # automatically when the function returns!
                backtrack(index + 1, current_str + letter)
                
        # Start at index 0 with an empty string
        backtrack(0, "")
        
        return res