# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        res = True
        def dfs(root):
            nonlocal res
            if root is None:
                return 0 
            left = 1+dfs(root.left)
            right = 1+dfs(root.right)
            print(left,right)
            if abs(right-left) > 1:
                res= res and False
            else:
                res= True and res
            return max(left,right)
        dfs(root)
        return res