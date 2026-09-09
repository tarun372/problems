# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNodes(self, head):
        stack = []
        curr = head
        
        # 1. Walk through the list and use the stack to filter nodes
        while curr:
            # If the current node is BIGGER than the top of the stack, pop the stack!
            while stack and stack[-1].val < curr.val:
                stack.pop()
            
            # Add the current node to the stack
            stack.append(curr)
            curr = curr.next
            
        # 2. Rebuild the linked list using the nodes left in the stack
        for i in range(len(stack) - 1):
            stack[i].next = stack[i + 1]
            
        # 3. Make sure the very last node points to nothing
        stack[-1].next = None
        
        # 4. Return the new head (the bottom of the stack)
        return stack[0]