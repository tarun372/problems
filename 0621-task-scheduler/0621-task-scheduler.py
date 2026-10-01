class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_count = [0] * 26
        total_tasks = 0
        maxx = 0
        freq = 0
        
        
        for task in tasks:
            idx = ord(task) - 65
            task_count[idx] += 1
            total_tasks += 1
            
            
            if task_count[idx] > maxx:
                maxx = task_count[idx]
        
        
        for count in task_count:
            if count == maxx:
                freq += 1
        
        
        return max((n + 1) * (maxx - 1) + freq, total_tasks)