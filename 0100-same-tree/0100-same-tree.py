# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        def sameornot(p,q):
            if p is  None and q is  None:
                return True 
            
            if p is None and q is not None:
                return False 
            
            if p is not None and q is None:
                return False 
            
            if p.val!=q.val:
                return False 
            else:
                return sameornot(p.left , q.left) and sameornot(p.right , q.right)
        
        return sameornot(p , q)