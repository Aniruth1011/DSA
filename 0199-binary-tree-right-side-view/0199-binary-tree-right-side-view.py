# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        l = [root]
        r = []
        while l:
            num_of_nodes = len(l)
            nodes = [] 

            for i in range(num_of_nodes):
                node = l.pop(0)
                if node:
                    nodes.append(node.val)

                    if node.left:
                        l.append(node.left)
                    if node.right:
                        l.append(node.right)

            if len(nodes)>0:
                r.append(nodes[-1])
        
        return r 
