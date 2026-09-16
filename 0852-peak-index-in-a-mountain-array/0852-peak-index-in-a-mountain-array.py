class Solution:
    def peakIndexInMountainArray(self, arr: list[int]) -> int:
        start = 0
        end = len(arr) - 1
        
        # Notice we use `start < end` instead of `start <= end`
        while start < end:
            mid = start + (end - start) // 2
            
            # If the next element is greater, we are climbing up the mountain.
            # The peak must be to the right of mid.
            if arr[mid] < arr[mid + 1]:
                start = mid + 1
                
            # If the next element is smaller, we are going down the mountain.
            # The peak is either exactly at mid, or to the left of mid.
            else:
                end = mid
                
        # start and end will converge on the exact index of the peak
        return start