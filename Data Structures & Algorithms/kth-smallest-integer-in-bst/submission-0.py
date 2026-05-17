# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = []
        def dfs(root):
            if root is None:
                return 
            if len(res) == k:
             return 
            if root.left is None and root.right is None:
                res.append(root.val)
                return
            dfs(root.left)
          
            res.append(root.val)
            dfs(root.right)
        dfs(root)
        print(res)
        return res[k-1]
            
        