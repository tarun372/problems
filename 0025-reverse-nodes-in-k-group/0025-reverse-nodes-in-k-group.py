# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k == 1:
            return head

        dummy = ListNode(0, head)
        group_prev = dummy

        while True:
            # 1. Check if there are at least k nodes left
            kth = group_prev
            for _ in range(k):
                kth = kth.next
                if not kth:
                    return dummy.next  # Not enough nodes left, return head

            group_next = kth.next  # Store node after the k-group

            # 2. Reverse the k group (in-place)
            prev = group_next
            cur = group_prev.next
            
            while cur != group_next:
                nxt = cur.next
                cur.next = prev
                prev = cur
                cur = nxt

            # 3. Connect reversed group with previous part of list
            tmp = group_prev.next
            group_prev.next = kth
            group_prev = tmp