# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:

        def leftsum(node , dire):

            if node is None:
                return 0 

            if node.left is None and node.right is None:
                if dire == "l":
                    return node.val
            
            return leftsum(node.left , "l") + leftsum(node.right , "r")
        
        return leftsum(root.left , "l") + leftsum(root.right , "r")