# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is not None:
            return self.getMaxDepth(root,0)
        else:
            return 0

    def getMaxDepth(self,root,depth) ->int:
        if root is None:
            return depth
        return max( self.getMaxDepth(root.left,depth+1), self.getMaxDepth(root.right,depth+1))
