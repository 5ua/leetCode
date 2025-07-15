from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, num in enumerate(nums):
            remains = target - num
            if remains in nums[i+1:]:
                return [i, nums.index(remains, i+1)]


solution = Solution()
print(solution.twoSum([2,7,11,15], 9))