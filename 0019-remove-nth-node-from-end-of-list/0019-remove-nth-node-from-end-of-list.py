# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        forward_node=dummy
        backward_node=dummy
        for _ in range(n + 1):
            forward_node=forward_node.next

        while (forward_node is not None):
            forward_node=forward_node.next
            backward_node=backward_node.next
        
        backward_node.next=backward_node.next.next
        
        return dummy.next