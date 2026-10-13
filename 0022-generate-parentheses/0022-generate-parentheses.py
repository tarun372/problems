class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        res = []
        
        def backtrack(open_count, close_count, path_str):
            # Base Case: String is full
            if len(path_str) == 2 * n:
                res.append(path_str)
                return
                
            # Rule 1: We can still add an open bracket
            if open_count < n:
                backtrack(open_count + 1, close_count, path_str + "(")
                
            # Rule 2: We have more open brackets than closed ones
            if close_count < open_count:
                backtrack(open_count, close_count + 1, path_str + ")")
                
        backtrack(0, 0, "")
        return res