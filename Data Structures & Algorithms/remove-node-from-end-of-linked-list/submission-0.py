# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        tmp = ListNode(0, head)
        first = head
        second = tmp

        for _ in range(n):
            first = first.next

        while first:
            first = first.next
            second = second.next
        
        second.next = second.next.next

        return tmp.next

        