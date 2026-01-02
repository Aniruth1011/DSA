# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def find_len(self , head):
        c = 0 
        while head:
            head = head.next
            c += 1 
        return c
    
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        c = self.find_len(head)
        k = k % c
        if k == 0:
            return head
        
        head_copy = head
        for i in range(c - k - 1):
            head_copy = head_copy.next 
        
        remaining = head_copy.next  
        head_copy.next = None  

        end = remaining
        while end.next:
            end = end.next
        
        end.next = head 
        return remaining
