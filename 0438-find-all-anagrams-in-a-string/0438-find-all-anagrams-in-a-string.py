class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p)>len(s):
            return []
        
        pcount = {}
        window = {}

        for ch in p:
            pcount[ch] = pcount.get(ch,0)+1
        
        for ch in s[:len(p)]:
            window[ch] = window.get(ch,0)+1
        
        ans = []

        if window == pcount:
            ans.append(0)

        left = 0

        for right in range(len(p),len(s)):

            window[s[right]] = window.get(s[right],0)+1

            window[s[left]] -= 1
            if window[s[left]] == 0:
                del window[s[left]]
            
            left += 1

            if pcount == window:
                ans.append(left)

        return ans
        