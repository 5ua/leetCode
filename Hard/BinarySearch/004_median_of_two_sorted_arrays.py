from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Always binary search on the smaller array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        n1, n2 = len(nums1), len(nums2)
        total_len = n1 + n2
        half = (total_len + 1) // 2  # Left partition size

        low, high = 0, n1

        while low <= high:
            mid1 = (low + high) // 2  # Partition index for nums1
            mid2 = half - mid1  # Partition index for nums2

            # Edge-safe boundaries
            left1 = nums1[mid1 - 1] if mid1 > 0 else float('-inf')
            right1 = nums1[mid1] if mid1 < n1 else float('inf')
            left2 = nums2[mid2 - 1] if mid2 > 0 else float('-inf')
            right2 = nums2[mid2] if mid2 < n2 else float('inf')

            # Correct partition found
            if left1 <= right2 and left2 <= right1:
                if total_len % 2 == 1:
                    # Odd total length → median is max of lefts
                    return max(left1, left2)
                else:
                    # Even total length → average of max(lefts) & min(rights)
                    return (max(left1, left2) + min(right1, right2)) / 2
            elif left1 > right2:
                # Move partition left in nums1
                high = mid1 - 1
            else:
                # Move partition right in nums1
                low = mid1 + 1

        # Should never be reached for valid sorted input
        raise ValueError("Input arrays are not sorted correctly.")
