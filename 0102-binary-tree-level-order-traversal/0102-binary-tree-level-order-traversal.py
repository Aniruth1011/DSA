# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if root is None:
            return []
        
        r= []
        l = [root]
        while l:
            level_l = len(l)
            level_nodes = []

            for i in range(level_l):
                node = l.pop(0)
                level_nodes.append(node.val)
                if node.left:
                    l.append(node.left)
                if node.right:
                    l.append(node.right)
            
            r.append(level_nodes)
        
        return r