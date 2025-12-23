# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:

        dic = {val : idx for idx , val in enumerate(inorder)}

        def build(postleft , postright , inorder_left , inorder_right):

            if postright < postleft:
                return None 

            root = postorder[postright]
            node = TreeNode(root)

            inorder_index = dic[root]

            left_size = inorder_index - inorder_left 

            node.left = build(postleft, postleft + left_size - 1, inorder_left, inorder_index - 1)
            node.right = build(postleft + left_size, postright - 1, inorder_index + 1, inorder_right)

            return node 
        
        return build(0 , len(postorder)-1 , 0 , len(inorder)-1)