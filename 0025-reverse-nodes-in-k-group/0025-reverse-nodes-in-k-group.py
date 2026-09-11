class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        group_prev = dummy

        while True:
            # Find the k-th node
            kth = group_prev
            for _ in range(k):
                kth = kth.next
                if not kth:
                    return dummy.next

            group_next = kth.next

            # Reverse group (in-place)
            prev, cur = group_next, group_prev.next
            while cur != group_next:
                nxt = cur.next
                cur.next = prev
                prev = cur
                cur = nxt

            # Reconnect outer pointers
            tmp = group_prev.next
            group_prev.next = kth
            group_prev = tmp