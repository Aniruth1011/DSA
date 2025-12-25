# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:

        def build(nums):
            n = len(nums)
            if n == 0:
                return 
            root = nums[n//2]

            left = nums[:n//2]
            right = nums[n//2+1:]

            root_node = TreeNode(root)
            root_node.left = build(left)
            root_node.right = build(right)

            return root_node 
        
        return build(nums)