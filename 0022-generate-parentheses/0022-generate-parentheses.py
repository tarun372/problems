class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        
        # We turn the backtracking function into a Generator using 'yield'
        def generate(open_count, close_count, path):
            # Base Case: When the string is done, 'yield' it out
            if len(path) == 2 * n:
                yield path
                return
                
            # Decision 1: Add '('
            if open_count < n:
                # 'yield from' bubbles the generated strings up the call stack
                yield from generate(open_count + 1, close_count, path + '(')
                
            # Decision 2: Add ')'
            if close_count < open_count:
                yield from generate(open_count, close_count + 1, path + ')')
                
        # list() consumes the generator all at once, taking memory only at the very end
        return list(generate(0, 0, ""))