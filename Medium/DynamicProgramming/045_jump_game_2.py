from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        # Edge case: if array has only one element, no jumps needed
        if len(nums) <= 1:
            return 0

        jumps = 0  # Number of jumps made
        current_end = 0  # End of the range for current jump
        farthest = 0  # Farthest position we can reach

        # We don't need to jump from the last index
        for i in range(len(nums) - 1):
            # Update the farthest position we can reach from current index
            farthest = max(farthest, i + nums[i])

            # If we've reached the end of current jump range
            if i == current_end:
                jumps += 1  # Make a jump
                current_end = farthest  # Update the range to farthest reachable

                # Early exit: if we can reach the last index
                if current_end >= len(nums) - 1:
                    break

        return jumps