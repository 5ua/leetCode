from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        Searches for a target in a rotated sorted array using modified binary search.
        Returns the index if found, otherwise -1.
        Time complexity: O(log n), Space: O(1).
        """
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            # Found target
            if nums[mid] == target:
                return mid

            # Case 1: Left half is sorted
            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1  # Target in left half
                else:
                    left = mid + 1   # Target in right half
            # Case 2: Right half is sorted
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1   # Target in right half
                else:
                    right = mid - 1  # Target in left half

        # Target not found
        return -1
