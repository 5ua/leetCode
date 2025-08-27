from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()  # Sort the array for two-pointer technique

        for i in range(len(nums)):
            # Skip duplicate values for the first element
            if i > 0 and nums[i] == nums[i-1]:
                continue

            j, k = i + 1, len(nums) - 1
            while j < k:
                total = nums[i] + nums[j] + nums[k]

                if total > 0:
                    k -= 1  # Move right pointer to reduce the sum
                elif total < 0:
                    j += 1  # Move left pointer to increase the sum
                else:
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1

                    # Skip duplicate values for the second element
                    while j < k and nums[j] == nums[j-1]:
                        j += 1

                    # Skip duplicate values for the third element
                    while j < k and nums[k] == nums[k+1]:
                        k -= 1

        return res
