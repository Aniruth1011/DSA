# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        node = head 
        node2 = head
        duplicates = set()
        while node and node.next:
            if node.val == node.next.val:
                duplicates.add(node.val)
            node = node.next 
        
        while head and head.val in duplicates:
            head = head.next 

        while node2  and node2.next :
            if node2.next.val in duplicates:
                node2.next = node2.next.next
            else:
                node2 = node2.next
            
        return head 

        