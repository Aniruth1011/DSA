# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def valid(root , alpha , beta):

            if root is None:
                return True 
            
            if root.left:
                if not ((alpha < root.left.val) and (root.left.val < root.val)):
                    return False
            
            if root.right:
                if not((root.val < root.right.val) and (root.right.val < beta)):
                    return False 
            
            return valid(root.left , alpha , root.val) and valid(root.right , root.val , beta)

        return valid(root , float('-inf') , float('inf'))
