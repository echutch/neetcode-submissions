# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:   
    def merge(self, list1, list2):
        p1, p2 = list1, list2
        head = curr = ListNode()

        while p1 and p2:
            if p1.val < p2.val:
                curr.next = p1
                p1 = p1.next
            else:
                curr.next = p2
                p2 = p2.next
            curr = curr.next
        curr.next = p1 or p2

        return head.next

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        n = len(lists)
        m = n // 2

        if m < 1:
            return lists[0]

        left = self.mergeKLists(lists[0:m])
        right = self.mergeKLists(lists[m:n])
        return self.merge(left, right)
        