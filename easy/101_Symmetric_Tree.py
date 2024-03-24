# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self._isSymmetric(root.left, root.right)

    def _isSymmetric(self, p, q) :
        if not p and not q : return True

        if p and q and p.val == q.val :
            return self._isSymmetric(p.left, q.right) and self._isSymmetric(p.right, q.left)
        return False