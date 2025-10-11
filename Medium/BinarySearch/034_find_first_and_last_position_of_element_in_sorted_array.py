from typing import List
# This approach uses binary search twice:
# - The first pass finds the leftmost (first) occurrence of the target.
# - The second pass finds the rightmost (last) occurrence of the target.
# Both searches operate in O(log n), making this efficient for sorted arrays.
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # Helper function to find the first index >= target
        def findBound(isFirst):
            left, right = 0, len(nums) - 1
            bound = -1

            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    bound = mid
                    # If searching for first occurrence, move left
                    if isFirst:
                        right = mid - 1
                    # Otherwise, move right to find the last occurrence
                    else:
                        left = mid + 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return bound

        first = findBound(True)
        last = findBound(False)
        return [first, last]
