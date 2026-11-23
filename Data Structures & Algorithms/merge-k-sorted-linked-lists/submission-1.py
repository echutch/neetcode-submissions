# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        min_heap = []
        id = 0

        for lst in lists:
            if lst:
                heapq.heappush(min_heap, (lst.val, id, lst))
                id += 1

        head = ListNode(0)
        curr = head

        while min_heap:
            nxt_val, _, nxt = heapq.heappop(min_heap)
            curr.next = nxt
            curr = curr.next

            if nxt.next:
                heapq.heappush(min_heap, (nxt.next.val, id, nxt.next))
                id += 1

        return head.next
        