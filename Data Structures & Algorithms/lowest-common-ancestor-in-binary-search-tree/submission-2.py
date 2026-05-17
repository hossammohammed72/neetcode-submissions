# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from numpy import union1d
class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        pancestors = self.getAnscestors(root,p,[])
        qancestors = self.getAnscestors(root,q,[])
        commonAncestors = [value for value in pancestors if value in qancestors]
        return TreeNode(list(commonAncestors).pop())


    def getAnscestors(self,root: TreeNode,node: TreeNode,ancestorsList:List[int])->TreeNode:
        if root is None:
             return None
        ancestorsList.append(root.val)
        if root.val == node.val:
            return ancestorsList
        elif node.val > root.val:
            return self.getAnscestors(root.right,node,ancestorsList)
        else:
            return self.getAnscestors(root.left,node,ancestorsList)





        