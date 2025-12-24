# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None:
            return TreeNode(val)
        head = root 
        def insert(root , val): 
            while True:
                if val < root.val:
                    if root.left is not None:
                        root = root.left 
                    else:
                        root.left = TreeNode(val)
                        break 
                elif val > root.val:
                    if root.right is not None:
                        root = root.right 
                    else:
                        root.right = TreeNode(val)
                        break 

        insert(root , val)
        return head                
