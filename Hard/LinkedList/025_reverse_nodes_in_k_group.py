from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """
        Iterative version of reversing nodes in k-group.
        This avoids recursion depth issues for very long lists.
        """

        if not head or k == 1:
            return head

        # Dummy node to simplify head handling
        dummy = ListNode(0, head)
        group_prev = dummy

        while True:
            # Find the k-th node from group_prev
            kth = group_prev
            for _ in range(k):
                kth = kth.next
                if not kth:
                    # Less than k nodes remaining, we are done
                    return dummy.next

            group_next = kth.next  # Node after the k-group

            # Reverse the group between group_prev.next and kth
            prev = group_next
            cur = group_prev.next
            while cur != group_next:
                next_node = cur.next
                cur.next = prev
                prev = cur
                cur = next_node

            # Now prev is the new head of the reversed group
            # Connect previous part with the reversed group
            temp = group_prev.next       # This will become the tail after reverse
            group_prev.next = prev
            group_prev = temp            # Move group_prev to the end of the reversed group
