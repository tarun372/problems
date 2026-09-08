class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        # Map every closing bracket to its corresponding opening bracket
        pairs = {')': '(', '}': '{', ']': '['}

        for ch in s:
            # If the character is an opening bracket, add it to the stack
            if ch not in pairs:
                st.append(ch)
            
            # If it IS a closing bracket...
            else:
                # 1. Check if the stack is already empty (e.g., string starts with ']')
                # 2. Check if the top of the stack DOESN'T match the required opening bracket
                if not st or st[-1] != pairs[ch]:
                    return False # We can fail immediately!
                
                # If it's a perfect match, pop the opening bracket
                st.pop()

        return not st