class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        res = []
        stack = [] # We use this to build the string piece by piece
        
        def backtrack(open_count, close_count):
            
            # 1. Base Case: If we have 'n' open and 'n' close, we are done
            if open_count == n and close_count == n:
                res.append("".join(stack))
                return
                
            # 2. Add an Open bracket (if we still have some left)
            if open_count < n:
                stack.append("(")                        # Choose
                backtrack(open_count + 1, close_count)   # Explore
                stack.pop()                              # Un-choose
                
            # 3. Add a Close bracket (if there are unpaired open brackets)
            if close_count < open_count:
                stack.append(")")                        # Choose
                backtrack(open_count, close_count + 1)   # Explore
                stack.pop()                              # Un-choose
                
        # Start with 0 open and 0 closed brackets
        backtrack(0, 0)
        return res