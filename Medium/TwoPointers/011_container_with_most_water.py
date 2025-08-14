from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        left, right = 0, len(height) - 1

        while left < right:
            current_area = (right - left) * min(height[left], height[right])
            if current_area > max_area:
                max_area = current_area

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area
