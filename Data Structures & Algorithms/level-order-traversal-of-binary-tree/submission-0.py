# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        levelsArray = {}
        def dfs(node,level):
            if node is None:
                return
            if level not in levelsArray:
                levelsArray[level] = [node.val]
            else:
                levelsArray[level].append(node.val)
            dfs(node.left,level+1)
            dfs(node.right,level+1)
        dfs(root,0)
        return list(levelsArray.values())
        