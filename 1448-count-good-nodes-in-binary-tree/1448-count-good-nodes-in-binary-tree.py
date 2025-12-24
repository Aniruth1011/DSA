# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def count(node , max_val):
            if node is None:
                return 0 
            
            if node.val < max_val:
                return count(node.left , max_val) + count(node.right , max_val)
            else:
                max_val = node.val
                return 1 + count(node.left , max_val) + count(node.right , max_val)
            
            #return count(node.left , max_val) + count(node.right , max_val)

            #return count(root.left , max_val) + count(root.right , max_val)
        
        if root:
            return count(root , -float('inf')) 
        else:
            return 0 
