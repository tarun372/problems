# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # head = [5, 2, 13, 3, 8]
        #         ^
        #                ^
        # 5 -> 2 -> 13 -> 3 -> 8
        # 3 <- 2 <- 13 <- 3 <- 8

        def reverse(nodeHead):
            prev = None
            curr = nodeHead
            while curr:
                nextNode = curr.next
                curr.next = prev
                prev = curr
                curr = nextNode
            return prev
        
        revHead = reverse(head)
        curr = revHead
        maxSeen = curr.val

        while curr.next:
            if curr.next.val < maxSeen:
                curr.next = curr.next.next
            else:
                maxSeen = curr.next.val
                curr = curr.next

        
        return reverse(revHead)