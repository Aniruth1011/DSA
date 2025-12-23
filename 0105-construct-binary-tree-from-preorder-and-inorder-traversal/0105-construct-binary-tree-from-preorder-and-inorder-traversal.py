# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        def build(preorder , inorder):

            if not preorder or not inorder:
                return None
            dic = {val : idx for idx , val in enumerate(inorder)}
            root = preorder[0]
            Node = TreeNode(root)

            root_index = dic[root]

            left_inorder = inorder[:root_index]
            right_inorder = inorder[root_index+1:] 

            left_preorder = preorder[1:len(left_inorder)+1]
            right_preorder = preorder[len(left_inorder)+1 :]

            Node.left = build(left_preorder ,left_inorder )
            Node.right = build(right_preorder , right_inorder )

            return Node 
        
        return build(preorder, inorder)

