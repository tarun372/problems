class Solution:
    def longestPalindrome(self, s: str) -> int:
        char_count = {}
        for c in s:
            char_count[c] = char_count.get(c, 0) + 1

        length = 0
        has_odd = False
        
        for count in char_count.values():
            if count % 2 == 0:
                length += count
            else:
                length += count - 1
                has_odd = True
        
        if has_odd:
            length += 1
        
        return length         