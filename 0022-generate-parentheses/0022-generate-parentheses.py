class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        res = []
        
        def backtrack(open_count, close_count, path):
            # 1. Base Case: If our string has 2n characters, we are done
            if len(path) == 2 * n:
                res.append("".join(path))
                return
                
            # 2. Decision 1: Add an Open Parenthesis
            if open_count < n:
                path.append("(")              # Choose
                backtrack(open_count + 1, close_count, path)  # Explore
                path.pop()                    # Un-choose (Backtrack!)
                
            # 3. Decision 2: Add a Close Parenthesis
            if close_count < open_count:
                path.append(")")              # Choose
                backtrack(open_count, close_count + 1, path)  # Explore
                path.pop()                    # Un-choose (Backtrack!)
                
        # Start with 0 open, 0 close, and an empty path
        backtrack(0, 0, [])
        return res