# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traverse(self , node , l):
        c = 0 
        while (c < l):
            node = node.next 
            c+=1 
        return node

    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]: 

        l = 0 
        temp = head 
        while temp:
            l+=1 
            temp = temp.next 
        
        def convert(left , right , head ):
            if (left > right):
                return None 
            l = (left + right)
            mid = l//2
            root_node = self.traverse(head , mid - left )
            root = TreeNode(root_node.val)
            root.left = convert(left , mid - 1, head)
            root.right = convert(mid+1 , right , root_node.next)

            return root
        
        return convert(0 , l-1 , head )
