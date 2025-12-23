# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        r = []
        l = [root]
        
        left2right = True 

        while l:
            numofnodes = len(l)
            nodes = []
            for i in range(numofnodes):
                node = l.pop(0)
                if node is not None:
                    nodes.append(node.val)
                else:
                    continue 
                if node.left:
                    l.append(node.left)
                if node.right:
                    l.append(node.right)
            if left2right:
                r.append(nodes)
                left2right = False
            else:
                r.append(nodes[::-1])
                left2right = True 
        
        return r