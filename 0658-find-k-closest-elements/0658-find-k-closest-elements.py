class Solution:
    def findClosestElements(self, arr: list[int], k: int, x: int) -> list[int]:
        # The window must start somewhere between index 0 and len(arr) - k
        left = 0
        right = len(arr) - k
        
        while left < right:
            mid = (left + right) // 2
            
            # mid is our guess for the start of the window.
            # mid + k is the element sitting JUST OUTSIDE the right edge of our window.
            # We compare the distance from x to the left edge vs x to the right edge.
            
            if x - arr[mid] > arr[mid + k] - x:
                # x is closer to the element outside the right edge than the left edge.
                # This means our window is too far left. Shift right.
                left = mid + 1
            else:
                # x is closer to the left edge (or they are tied).
                # The prompt states if distances are tied, the smaller number wins.
                # Since the array is sorted, the left side is always smaller. Shift left.
                right = mid
                
        # left is now perfectly locked onto the start of our window
        return arr[left:left + k]