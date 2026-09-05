class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        prefix_sum = {0:-1}
        current_len = 0
        current_sum = 0
        max_len = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                current_sum -= 1
            else:
                current_sum += 1
            
            if current_sum in prefix_sum:
                current_len = i - prefix_sum[current_sum]
            else:
                prefix_sum[current_sum] = i
            max_len = max(max_len,current_len)
        return max_len
        