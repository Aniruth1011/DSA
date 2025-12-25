# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        memo = defaultdict(int)
        def subtreesum(node):
            if node is None:
                return 0 
                        
            subtreesum_ = node.val +  subtreesum(node.left) + subtreesum(node.right)
            memo[subtreesum_]+=1 

            return subtreesum_
        
        subtreesum(root)

        max_count = max(memo.values(), default=0)
        res = [key for key, value in memo.items() if value == max_count]
        
        return res