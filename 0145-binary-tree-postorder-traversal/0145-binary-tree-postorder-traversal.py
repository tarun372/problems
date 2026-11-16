class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> list[int]:
        res = []
        
        def dfs(node):
            if not node:
                return
                
            # 1. Traverse the entire LEFT subtree
            dfs(node.left)
            
            # 2. Traverse the entire RIGHT subtree
            dfs(node.right)
            
            # 3. Visit the ROOT last (append its value)
            res.append(node.val)
            
        dfs(root)
        return res