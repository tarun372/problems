class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        for i in range(2,len(arr)):
            if arr[i]<arr[i-1] and arr[i-1]>arr[i-2]:
                return i-1
                break
        