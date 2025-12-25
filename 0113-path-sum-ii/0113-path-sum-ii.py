# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:

        list_of_paths = []

        def find_paths(node , curr_sum , path):
            if node is None:
                return 
            curr_sum+=node.val 
            path.append(node.val)

            if ( node.left is None ) and (node.right is None) and (curr_sum == targetSum):
                list_of_paths.append(path.copy())
            
            find_paths(node.left , curr_sum , path)
            find_paths(node.right , curr_sum , path)

            path.pop()

        find_paths(root , 0, []) 

        return list_of_paths
