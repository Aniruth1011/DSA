# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:

        def convert(nums):
            if len(nums) == 0:
                return None 

            root = TreeNode(nums[len(nums)//2] )
            root.left = convert(nums[:len(nums)//2])
            root.right = convert(nums[len(nums)//2 + 1 : ])

            return root 
        
        return convert(nums)