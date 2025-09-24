from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        path = []

        def backtrack(left: int, right: int):
            # If the current sequence is complete
            if len(path) == n * 2:
                res.append("".join(path))
                return

            # Add '(' if we still have left parentheses available
            if left < n:
                path.append('(')
                backtrack(left + 1, right)
                path.pop()  # Backtrack

            # Add ')' if it does not exceed the number of '('
            if right < left:
                path.append(')')
                backtrack(left, right + 1)
                path.pop()  # Backtrack

        backtrack(0, 0)
        return res
