# Definition for a binary tree node.
from typing import Optional

import null


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if not node:
                # An empty subtree is balanced with height 0
                return (True, 0)

            # Recursively check the left subtree
            left_balanced, left_depth = dfs(node.left)
            if not left_balanced:
                # If left subtree is unbalanced, no need to check further
                return (False, 0)

            # Recursively check the right subtree
            right_balanced, right_depth = dfs(node.right)
            if not right_balanced:
                # If right subtree is unbalanced, no need to check further
                return (False, 0)

            # A node is balanced if both subtrees are balanced and
            # the height difference is no more than 1
            is_balanced = abs(left_depth - right_depth) <= 1
            depth = 1 + max(left_depth, right_depth)

            return (is_balanced, depth)

        # Start DFS from the root and return the balanced status
        return dfs(root)[0]
