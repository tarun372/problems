class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        totalSum = sum(nums)
        leftSum = 0
        
        for i, num in enumerate(nums):
            if leftSum == totalSum - leftSum - num:
                return i
            leftSum += num
            
        return -1