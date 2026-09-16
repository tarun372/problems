class Solution(object):
    def findMin(self, nums):

        right = nums[-1]
        low, high = 0, len(nums)-1

        while low < high:
            mid = (low + high) //2
            if nums[mid] <= right:
                high = mid
            else:
                low = mid + 1
        return nums[low]