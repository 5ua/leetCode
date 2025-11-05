from functools import lru_cache

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        """
        Returns True if string s matches pattern p.
        '.'  -> matches any single character
        '*'  -> matches zero or more of the preceding element
        """

        @lru_cache(None)
        def dfs(i, j):
            # Base case: reached end of pattern
            if j == len(p):
                return i == len(s)

            # Check if first character matches
            first_match = (i < len(s)) and (p[j] == s[i] or p[j] == '.')

            # If next char in pattern is '*', handle zero or more occurrences
            if j + 1 < len(p) and p[j + 1] == '*':
                # Case 1: skip "x*" (treat as zero occurrences)
                # Case 2: if first chars match, use one occurrence of p[j]
                return dfs(i, j + 2) or (first_match and dfs(i + 1, j))
            else:
                # Move both pointers if current chars match
                return first_match and dfs(i + 1, j + 1)

        return dfs(0, 0)
