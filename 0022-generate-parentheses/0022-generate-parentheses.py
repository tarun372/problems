class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        res = []
        
        # 1. Pre-allocate an array of exact size (2 * n) with empty strings.
        # This completely eliminates dynamic memory resizing overhead.
        path = [''] * (2 * n)
        
        # 2. Track the current 'index' we are overwriting
        def backtrack(index, open_count, close_count):
            
            # Base Case: We filled all available slots
            if index == 2 * n:
                res.append("".join(path))
                return
            
            # Decision 1: Add '('
            if open_count < n:
                path[index] = '('  # Pure O(1) memory overwrite
                backtrack(index + 1, open_count + 1, close_count)
                
            # Decision 2: Add ')'
            if close_count < open_count:
                path[index] = ')'  # Overwrites the '(' if we backtracked!
                backtrack(index + 1, open_count, close_count + 1)
                
        # Start at index 0, with 0 open and 0 close
        backtrack(0, 0, 0)
        return res