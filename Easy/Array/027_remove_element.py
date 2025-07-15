from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        idx = 0
        while(idx < len(nums)):
            if nums[idx] == val: del nums[idx]
            else: idx += 1
        return len(nums)


solution = Solution()
print(solution.removeElement(nums = [0,1,2,2,3,0,4,2], val = 2))