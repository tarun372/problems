class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        # 1. Count the frequencies of each number
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
            
        # 2. Create buckets where the index is the frequency.
        # The maximum possible frequency is the length of the array itself.
        buckets = [[] for _ in range(len(nums) + 1)]
        
        # Put the numbers into their respective frequency buckets
        for num, freq in count.items():
            buckets[freq].append(num)
            
        # 3. Walk backwards from the highest possible frequency to gather the top K
        res = []
        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                res.append(num)
                if len(res) == k:
                    return res
                    
        return res