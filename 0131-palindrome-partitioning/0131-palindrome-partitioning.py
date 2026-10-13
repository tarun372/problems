class Solution:
    def partition(self, s: str) -> list[list[str]]:
        res = []
        path = []
        
        def backtrack(start_index):
            # 1. Base Case: If our pointer reaches the end of the string,
            # it means every chunk we chopped off was a valid palindrome.
            if start_index == len(s):
                res.append(path[:])  # Deep copy the valid partition
                return
                
            # 2. Iterate through all possible endings for our current prefix
            for i in range(start_index, len(s)):
                
                # Chop off the prefix from 'start_index' to 'i'
                substring = s[start_index:i+1]
                
                # PRUNING: Only explore this branch if the prefix is a palindrome
                if substring == substring[::-1]:
                    
                    # CHOOSE
                    path.append(substring)
                    
                    # EXPLORE (move the pointer past the chunk we just chopped off)
                    backtrack(i + 1)
                    
                    # UN-CHOOSE (Backtrack)
                    path.pop()
                    
        # Kick off recursion at index 0
        backtrack(0)
        return res