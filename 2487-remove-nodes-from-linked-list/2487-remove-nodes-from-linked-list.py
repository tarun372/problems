class Solution:
    def removeNodes(self, head):
        stack = []
        curr = head
        
        # Phase 1: Filter out the smaller nodes using the stack
        while curr:
            # If the new node is BIGGER than the top of our stack, rip up the top note!
            while stack and stack[-1].val < curr.val:
                stack.pop()
            
            # Put the current node on the stack
            stack.append(curr)
            curr = curr.next
            
        # Phase 2: Link the surviving nodes back together
        for i in range(len(stack) - 1):
            stack[i].next = stack[i+1]
            
        # Make sure the very last node points to nothing
        stack[-1].next = None
        
        # The bottom of the stack is the new head of our linked list
        return stack[0]