# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        odd = head
        even= head.next
        odd_ptr = odd
        even_ptr = even

        while even_ptr and even_ptr.next is not None:
            odd_ptr.next= odd_ptr.next.next
            odd_ptr=odd_ptr.next
            even_ptr.next = even_ptr.next.next
            even_ptr=even_ptr.next
        odd_ptr.next = even
        
        return odd
