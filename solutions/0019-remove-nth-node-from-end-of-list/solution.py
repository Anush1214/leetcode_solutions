# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr=head
        prev=0
        while curr:
            prev+=1
            curr=curr.next
        if prev==n:
            return head.next
        curr=head
        new=prev-n-1
        while new>0:
            curr = curr.next
            new-=1
        curr.next=curr.next.next

        return head
