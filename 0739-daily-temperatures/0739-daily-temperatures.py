class Solution:
    def dailyTemperatures(self, temps: List[int]) -> List[int]:
        stack = []
        result = [0] * len(temps)

        for i, t in enumerate(temps):
            while stack and temps[stack[-1]] < t:
                index = stack.pop()
                result[index] = i - index

            stack.append(i)

        return result