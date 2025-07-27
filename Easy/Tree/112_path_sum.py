# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # Base case: if the node is None, there's no path
        if not root:
            return False

        # If the node is a leaf, check if the remaining targetSum equals the node's value
        if not root.left and not root.right:
            return root.val == targetSum

        # Recursively check left and right subtrees with updated targetSum
        left_has_path = self.hasPathSum(root.left, targetSum - root.val)
        right_has_path = self.hasPathSum(root.right, targetSum - root.val)

        # Return True if either left or right subtree has a valid path
        return left_has_path or right_has_path