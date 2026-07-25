class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        size = len(nums)
        
        def jump(current: int):
            jump = current + nums[current]
            return jump % size

        def checkCycle(target: int):
            sign = nums[target] > 0
            cycleSize = 1
            ptr = jump(target)
            while ptr != target:
                cycleSize += 1
                if (nums[ptr] > 0) != sign:
                    return False

                ptr = jump(ptr)

            return cycleSize > 1

        visited = set()
        for i in range(size):
            if i in visited:
                continue

            visited.add(i)

            slow = fast = i
            while True:
                slow = jump(slow)
                fast = jump(jump(fast))
                visited.add(slow)
                visited.add(fast)
                if slow == fast:
                    if checkCycle(slow):
                        return True
                    break
        
        return False