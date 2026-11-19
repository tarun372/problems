from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> list[list[int]]:
        if not root:
            return []
            
        res = []
        queue = deque([root])  # Start with the root in the queue
        
        while queue:
            level = []
            level_size = len(queue)  # Snapshot: exact number of nodes on THIS level
            
            # Process only the nodes belonging to the current level
            for _ in range(level_size):
                node = queue.popleft()  # O(1) pop from the front
                level.append(node.val)
                
                # Add children to the back of the queue for the NEXT level
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                    
            res.append(level)
            
        return res