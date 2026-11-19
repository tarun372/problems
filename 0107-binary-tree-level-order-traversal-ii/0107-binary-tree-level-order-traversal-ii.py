class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> list[list[int]]:
        if not root:
            return []
            
        res = []
        curr_level = [root]
        
        while curr_level:
            next_level = []
            vals = []
            
            for node in curr_level:
                vals.append(node.val)
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
                    
            res.append(vals)
            curr_level = next_level
            
        # Flip the floors so the bottom level comes first
        return res[::-1]