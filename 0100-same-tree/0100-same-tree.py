# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        def sametree(p , q , t):

            if p is None and q:
                return False 
            
            if p and (q is None):
                return False
            if p and q:
                if p.val != q.val:
                    return False   

                return (sametree(p.left , q.left , "l")) and (sametree(p.right , q.right , "r")) 

            return True

        return sametree(p , q , "ro")