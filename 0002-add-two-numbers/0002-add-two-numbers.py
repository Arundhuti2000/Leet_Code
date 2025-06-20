# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev=None
        while (head):
            nextNode= head.next
            head.next= prev
            prev=head
            head=nextNode
        return prev
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # l1=self.reverseList(l1)
        # l2=self.reverseList(l2)
        head=ListNode()
        final=head
        carry=0
        while(l1 or l2 or carry):
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            sum_of_curr_digits= val1+val2+carry
            curr_digit= sum_of_curr_digits%10
            carry=sum_of_curr_digits//10
            final.next=ListNode(curr_digit)
            final=final.next
            if l1:
                l1=l1.next
            if l2:
                l2=l2.next
        return head.next