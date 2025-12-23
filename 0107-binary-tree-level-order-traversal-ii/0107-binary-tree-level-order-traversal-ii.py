# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:

        if root is None:
            return []
        r = []
        l = [root] 

        while l:
            num_of_nodes = len(l)
            nodes = []

            for i in range(num_of_nodes):
                node = l.pop(0) 
                nodes.append(node.val)
                if node.left:
                    l.append(node.left)
                if node.right:
                    l.append(node.right)
                
            r.append(nodes)
        
        return r[::-1]