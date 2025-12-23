# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def height(self , node):
        if node is None:
            return 0 
        return 1 + max(self.height(node.left) , self.height(node.right))

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def isbalanced(root):

            if root is None:
                return True 
            
            l_h = self.height(root.left)
            r_h = self.height(root.right)
            print(l_h , r_h)
            if abs(l_h - r_h)>1:
                return False 
            else:
                return self.isBalanced(root.left) and self.isBalanced(root.right)
            
        return isbalanced(root)      