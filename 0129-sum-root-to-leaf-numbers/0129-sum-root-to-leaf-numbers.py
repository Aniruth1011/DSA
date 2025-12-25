# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:

        def dfs(node , num):
            if node:
                if node.left is None and node.right is None:
                    return int(num + str(node.val))
            if node is None:
                return 0
            
            return dfs(node.left , num + str(node.val)) +  dfs(node.right , num + str(node.val))
    
        return dfs(root , "")