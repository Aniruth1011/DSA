# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:

        def convert(left , right):
            if (left > right):
                return None 
            
            root = TreeNode(nums[(left+right)//2])
            root.left = convert(left , (left+right)//2 - 1)
            root.right = convert((left+right)//2 + 1 , right)

            return root 
        
        return convert(0 , len(nums)-1)