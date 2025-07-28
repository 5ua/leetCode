# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode(0)  # Dummy node to simplify list construction
        current = dummy_head
        carry = 0  # Initialize carry for addition

        # Loop through both lists until both are exhausted and no carry remains
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0  # Get current value of l1 node or 0
            val2 = l2.val if l2 else 0  # Get current value of l2 node or 0
            total = val1 + val2 + carry  # Add both values and the carry

            carry = total // 10  # Update carry for next digit
            current.next = ListNode(total % 10)  # Create new node with current digit
            current = current.next  # Move to next node

            # Advance l1 and l2 if not at the end
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return dummy_head.next  # Return the next node after dummy (head of result)r
