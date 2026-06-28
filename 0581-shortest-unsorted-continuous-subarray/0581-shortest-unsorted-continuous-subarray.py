class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        greatest = float('-inf')
        smallest = float('inf')
        left = right = 0
        for i in range(n):
            if nums[i] >= greatest:
                greatest = nums[i]
            else:
                right = i

        for i in range(n - 1, -1, -1):
            if nums[i] <= smallest:
                smallest = nums[i]
            else:
                left = i

        return right - left + 1 if right != 0 or left != 0 else 0