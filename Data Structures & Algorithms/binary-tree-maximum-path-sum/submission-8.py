# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def dfs(root,top=False):
            if root is None:
                return 0
            if top:
                return  max(0,dfs(root.left,True),dfs(root.right,True))+root.val
            left = dfs(root.left,True)
            right = dfs(root.right,True)
            return max(root.val,right+left+root.val,right+root.val,left+root.val)
            
        queue = [root]
        i=0
        currentSum = float("-infinity")
        while i < len(queue):
            currentRoot = queue[i]
            i+=1    
            currentSum = max(currentSum, dfs(currentRoot))
            if currentRoot.left is not None:
                queue.append(currentRoot.left)
            if currentRoot.right is not None:
                queue.append(currentRoot.right)
        return currentSum

        