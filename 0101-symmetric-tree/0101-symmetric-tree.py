# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        def mirror(left , right):

            if (left is None ) and right is not None:
                return False 
            
            if (right is None) and (left is not None):
                return False 
            
            if (left is None) and (right is None):
                return True 
            return (left.val == right.val) and mirror(left.left , right.right) and mirror(left.right ,  right.left)

            return True 
        if not root:
            return True
        return mirror(root.left , root.right)