# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from itertools import permutations

class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        if n == 0:
            return []
        def build(start , end):
            trees = []
            if start > end:
                return [None]
            
            for i in range(start , end+1):
                left_trees = build(start , i-1)
                right_trees = build(i+1 , end)

                for l in left_trees:
                    for r in right_trees:
                        root = TreeNode(i)
                        root.left = l 
                        root.right = r 
                        trees.append(root)
            return trees
        
        return build(1 , n)