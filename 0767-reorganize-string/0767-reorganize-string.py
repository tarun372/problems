from collections import Counter

class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)
        
        # Find the absolute most frequent character
        max_char = max(count, key=count.get)
        max_cnt = count[max_char]
        
        # Pigeonhole Principle: If it appears too many times, it's impossible.
        if max_cnt > (len(s) + 1) // 2:
            return ""
            
        res = [''] * len(s)
        idx = 0
        
        # 1. Place the most frequent character at all the even indices first
        while count[max_char] > 0:
            res[idx] = max_char
            idx += 2
            count[max_char] -= 1
            
        # 2. Blindly fill the remaining spots with the other characters
        for char, cnt in count.items():
            while count[char] > 0:
                # If we reach the end of the array, wrap around to the odd indices
                if idx >= len(s):
                    idx = 1
                    
                res[idx] = char
                idx += 2
                count[char] -= 1
                
        return "".join(res)