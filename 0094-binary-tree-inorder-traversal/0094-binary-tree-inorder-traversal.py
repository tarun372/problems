class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> list[int]:
        res = []
        
        def dfs(node):
            # Base Case: If we hit an empty leaf, go back up
            if not node:
                return
                
            # 1. Traverse the entire LEFT subtree first
            dfs(node.left)
            
            # 2. Visit the ROOT (append its value)
            res.append(node.val)
            
            # 3. Traverse the entire RIGHT subtree last
            dfs(node.right)
            
        dfs(root)
        return res