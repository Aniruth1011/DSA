# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        inorder_list = []

        def inorder(root):
            if root is None:
                return 
            
            inorder(root.left)
            inorder_list.append(root)
            inorder(root.right)
        
        inorder(root)
        first = None 
        second = None
        for i in range(len(inorder_list)-1):
            if inorder_list[i].val > inorder_list[i+1].val:
                if not first:
                    first = inorder_list[i]
                second = inorder_list[i+1] 

        first.val, second.val = second.val , first.val 
                            
