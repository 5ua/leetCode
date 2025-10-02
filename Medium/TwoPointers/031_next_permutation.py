from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Rearranges numbers into the lexicographically next greater permutation.
        If such arrangement is not possible, it rearranges into the lowest possible order.
        Operates in-place with O(1) extra memory.
        """
        n = len(nums)

        # Step 1: Find the first index 'i-1' such that nums[i-1] < nums[i]
        # This identifies the pivot point
        i = n - 1
        while i > 0 and nums[i - 1] >= nums[i]:
            i -= 1

        # If no such pivot exists, nums are in descending order → reverse to smallest permutation
        if i == 0:
            nums.reverse()
            return

        # Step 2: Find the smallest number greater than nums[i-1] to the right
        j = n - 1
        while nums[j] <= nums[i - 1]:
            j -= 1

        # Step 3: Swap the pivot with nums[j]
        nums[i - 1], nums[j] = nums[j], nums[i - 1]

        # Step 4: Reverse the suffix starting at index i
        nums[i:] = reversed(nums[i:])
