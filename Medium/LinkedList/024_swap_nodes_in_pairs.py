# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Create a dummy node to simplify edge cases
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        # Traverse the list in pairs
        while prev.next and prev.next.next:
            first = prev.next  # First node in the pair
            second = first.next  # Second node in the pair

            # Swap the pair
            first.next = second.next
            second.next = first
            prev.next = second

            # Move prev pointer to the next pair
            prev = first

        return dummy.next
