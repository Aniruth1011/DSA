# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        result = []

        def backtrack(path , node):
            if node is None:
                return 

            path.append(str(node.val))

            if node.left is None and node.right is None:
                result.append("->".join(path))
            else:
                backtrack(path , node.left)
                backtrack(path , node.right)
            path.pop()
        
        backtrack([] , root)
        return result