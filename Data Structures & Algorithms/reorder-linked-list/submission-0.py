# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Split list into two halves
        slow, fast = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        # Reverse second half
        l2 = slow.next
        prev = slow.next = None

        while l2:
            next = l2.next
            l2.next = prev
            prev = l2
            l2 = next

        # Merge two lists
        l1, l2 = head, prev
        while l2:
            l1_next, l2_next = l1.next, l2.next
            l1.next = l2
            l2.next = l1_next
            l1 = l1_next
            l2 = l2_next