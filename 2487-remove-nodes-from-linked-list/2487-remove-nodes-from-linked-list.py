# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNodes(self, head):
        if not head:
            return None

        # Helper function to reverse a linked list
        def reverse_list(node):
            prev = None
            curr = node
            while curr:
                next_temp = curr.next
                curr.next = prev
                prev = curr
                curr = next_temp
            return prev

        # 1. Reverse the entire list
        head = reverse_list(head)

        # 2. Filter out the smaller nodes
        curr = head
        max_val = curr.val
        
        while curr.next:
            if curr.next.val < max_val:
                # The next node is too small! Skip it (delete it).
                curr.next = curr.next.next
            else:
                # The next node is big enough! Keep it and update max_val.
                curr = curr.next
                max_val = curr.val
                
        # 3. Reverse it back to normal
        return reverse_list(head)