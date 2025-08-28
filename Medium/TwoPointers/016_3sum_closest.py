from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        # Sort the array to apply the two-pointer technique
        nums.sort()
        # Initialize closest sum with a large value
        closest_sum = float("inf")

        for i in range(len(nums)):
            # Skip duplicate values for the first element
            if i > 0 and nums[i] == nums[i-1]:
                continue

            j, k = i + 1, len(nums) - 1
            while j < k:
                current_sum = nums[i] + nums[j] + nums[k]

                # Update closest_sum if current_sum is closer to the target
                if abs(current_sum - target) < abs(closest_sum - target):
                    closest_sum = current_sum

                if current_sum > target:
                    # Move the right pointer left to reduce the sum
                    k -= 1
                elif current_sum < target:
                    # Move the left pointer right to increase the sum
                    j += 1
                else:
                    # Exact match found; return immediately
                    return current_sum

        return closest_sum