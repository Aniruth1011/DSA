# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        def symmetric(left , right):

            if left is None and right is None:
                return True 
            
            if ( left is None ) and (right is not None):
                return False 
            
            if left is not None and right is None:
                return False 
            
            if (left.val!=right.val):
                return False 
            
            return symmetric(left.left , right.right) and symmetric(left.right , right.left) 
        
        return symmetric(root.left , root.right)