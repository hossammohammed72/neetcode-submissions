# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        def dfs(root,top=False):
            if root is None:
                return 0 
            if top:
                return 1+dfs(root.left)+dfs(root.right)
            return 1+max(dfs(root.left),dfs(root.right))
        res = 0
        q = deque()
        while root is not None:
            res = max(res,dfs(root,True))
            if root.left is not None:
                q.append(root.left)
            if root.right is not None:
                q.append(root.right)
            if len(q) > 0:
                root = q.pop()
            else:
                root = None
        return res-1

        