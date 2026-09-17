class Solution:
    def findMaxNSum(self, weights: list[int], low: int, high: int) -> tuple[int, int]:
        for w in weights:
            if low > w:
                low = w
            high += w
        return low, high

    def findMinWeights(self, weights: list[int], days: int, minWeight: int) -> bool:
        temp = minWeight
        i = 0
        while i < len(weights) and days > 0:
            if temp < weights[i]:
                days -= 1
                temp = minWeight
            else:
                temp -= weights[i]
                i += 1
        return i == len(weights)

    def shipWithinDays(self, weights: list[int], days: int) -> int:
        low, high = 0, 0
        low, high = self.findMaxNSum(weights, low, high)
        ans = 0
        while low <= high:
            mid = (low + high) // 2
            if self.findMinWeights(weights, days, mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans