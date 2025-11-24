from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        def backtrack(start, path, total):
            # If the sum equals the target, add the current path to the result
            if total == target:
                result.append(path[:])
                return

            # If the sum exceeds target, stop exploring this path
            if total > target:
                return

            # Try each candidate starting from 'start' to avoid duplicates
            for i in range(start, len(candidates)):
                path.append(candidates[i])  # Choose current candidate
                backtrack(i, path, total + candidates[i])  # Recurse, same index allows reuse
                path.pop()  # Backtrack

        backtrack(0, [], 0)
        return result
