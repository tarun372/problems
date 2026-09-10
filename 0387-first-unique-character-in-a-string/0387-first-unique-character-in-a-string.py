class Solution:
    def firstUniqChar(self, s: str) -> int:
        char_count = {}
        
        # Count the frequency of each character
        for char in s:
            char_count[char] = char_count.get(char, 0) + 1
        
        # Find the index of the first unique character
        for index, char in enumerate(s):
            if char_count[char] == 1:
                return index
        
        return -1  # Return -1 if no unique character is found