# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:

        to_left = ListNode(0)
        to_right = ListNode(0) 
        left = to_left 
        right = to_right 
        current = head 
        while current:
            if current.val < x:
                left.next = current 
                left = left.next 
            else:
                right.next = current 
                right = right.next

            current = current.next 

        right.next = None
        left.next = to_right.next 

        return to_left.next 
        
