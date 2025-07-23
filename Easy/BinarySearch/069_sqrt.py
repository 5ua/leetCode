class Solution:
    def mySqrt(self, x: int) -> int:
        left = 0
        right = x
        while left <= right:
            mid = (left + right) // 2
            if mid * mid < x:
                left = mid + 1
            elif x < mid * mid:
                right = mid - 1
            else:
                return mid

        return right



solution = Solution()
print(solution.mySqrt(5))