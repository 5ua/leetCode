from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtrack(path):
            # Base case: if the path contains all numbers
            if len(path) == len(nums):
                result.append(path[:])
                return

            for n in nums:
                # Skip numbers already used in the current permutation
                if n in path:
                    continue
                # Choose number and explore further
                path.append(n)
                backtrack(path)
                # Undo choice
                path.pop()

        backtrack([])
        return result