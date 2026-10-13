class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        res = []
        
        # Pass the string 's' directly. No lists, no append, no pop.
        def dfs(left, right, s):
            # Base case: length is exactly 2 * n
            if len(s) == n * 2:
                res.append(s)
                return
            
            # If we can add a left bracket
            if left < n:
                dfs(left + 1, right, s + '(')
                
            # If we can add a right bracket
            if right < left:
                dfs(left, right + 1, s + ')')
                
        dfs(0, 0, '')
        return res