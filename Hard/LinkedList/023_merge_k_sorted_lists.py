import heapq
from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        Merges k sorted linked lists into one sorted list.
        Uses a min-heap to efficiently get the smallest current node.
        Time Complexity: O(N log k), where N = total nodes, k = number of lists.
        """

        min_heap = []
        dummy = tail = ListNode(0)

        # Push the first node of each list into the heap
        for idx, node in enumerate(lists):
            if node:
                # Include index to avoid comparison issues when values are equal
                heapq.heappush(min_heap, (node.val, idx, node))

        # Extract the smallest element and push its next node
        while min_heap:
            val, idx, node = heapq.heappop(min_heap)
            tail.next = node
            tail = tail.next
            if node.next:
                heapq.heappush(min_heap, (node.next.val, idx, node.next))

        return dummy.next
