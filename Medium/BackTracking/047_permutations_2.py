from typing import List
from collections import Counter

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result = []
        counter = Counter(nums)  # Count occurrences of each number

        def backtrack(path):
            # Base case: if the path is a full permutation
            if len(path) == len(nums):
                result.append(path[:])  # Make a copy and store it
                return

            # Iterate over each unique number
            for num in counter:
                if counter[num] > 0:
                    # Choose the number
                    path.append(num)
                    counter[num] -= 1

                    # Recurse with updated state
                    backtrack(path)

                    # Undo the choice (backtrack)
                    path.pop()
                    counter[num] += 1

        backtrack([])
        return result