# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def dfs(root,subroot):
            if root is None and subroot is None:
                return True
            if subroot is None:
                return False
            if root is None:
                return False
            if root.val != subroot.val:
                return False
            return dfs(root.left,subroot.left) and dfs(root.right,subroot.right)        
        q = deque()
        res = False
        while root:
            if root.val == subRoot.val:
                res = res or dfs(root,subRoot)
            if root.left:
                q.append(root.left)
            if root.right:
                q.append(root.right)
            if len(q):
                root = q.pop()
            else:
                root = None
        return res
             
            
                
