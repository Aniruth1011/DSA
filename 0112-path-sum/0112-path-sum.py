# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        s = 0
        if root is None:
            return False
        def checkpathsum(root , s):
            if root is None:
                return False
            s+= root.val

            if root.left is None and root.right is None:
                if s == targetSum:
                    return True 
                return False            

            return checkpathsum(root.left, s) or checkpathsum(root.right,s)
        
        return checkpathsum(root , s)
            
