class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        i, j = 0, 0
        res = []
        
        while i < len(firstList) and j < len(secondList):
            # 1. Find the highest start time and the lowest end time
            start_max = max(firstList[i][0], secondList[j][0])
            end_min = min(firstList[i][1], secondList[j][1])
            
            # 2. If the start is before or equal to the end, they overlap!
            if start_max <= end_min:
                res.append([start_max, end_min])
            
            # 3. Move the pointer for the interval that ends FIRST
            if firstList[i][1] < secondList[j][1]:
                i += 1
            else:
                j += 1
                
        return res