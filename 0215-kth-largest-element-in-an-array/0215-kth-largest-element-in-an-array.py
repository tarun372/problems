class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        # Create an array to hold frequencies for numbers -10000 to 10000
        freq = [0] * 20001 
        
        # 1. Count frequencies (Offset by 10,000 to handle negative numbers)
        for num in nums:
            freq[num + 10000] += 1
            
        # 2. Walk backwards from the absolute largest possible number
        for i in range(20000, -1, -1):
            k -= freq[i]
            
            # The moment k hits 0 (or goes negative), we found our target
            if k <= 0:
                return i - 10000