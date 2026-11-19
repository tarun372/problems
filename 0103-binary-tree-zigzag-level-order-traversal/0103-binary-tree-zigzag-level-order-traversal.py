class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> list[list[int]]:
        if not root:
            return []
            
        res = []
        curr_level = [root]
        reverse = False
        
        while curr_level:
            next_level = []
            vals = []
            
            # Direct list iteration is much faster in Python than deque.popleft()
            for node in curr_level:
                vals.append(node.val)
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
                    
            res.append(vals[::-1] if reverse else vals)
            curr_level = next_level
            reverse = not reverse
            
        return res