from collections import deque

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> list[list[int]]:
        if not root:
            return []
            
        res = []
        queue = deque([root])
        left_to_right = True  # Tracks the current floor's direction
        
        while queue:
            level = []
            level_size = len(queue)
            
            for _ in range(level_size):
                node = queue.popleft()
                level.append(node.val)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                    
            # The Twist: Reverse the list on right-to-left floors
            if not left_to_right:
                level.reverse()
                
            res.append(level)
            left_to_right = not left_to_right  # Flip direction for the next floor
            
        return res