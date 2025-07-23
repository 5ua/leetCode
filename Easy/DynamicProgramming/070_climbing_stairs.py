class Solution:
    def climbStairs(self, n: int) -> int:
        #return sum(comb(n-d,d) for d in range(n//2+1))

        #f(n) = f(n-1) + f(n-2)
        if n == 0 or n == 1:
            return 1
        #f(0)=1, f(1)=1
        prev, curr = 1, 1
        for i in range(2, n + 1):
            curr = prev + curr
            prev = curr - prev
        return curr

solution = Solution()
print(solution.climbStairs(5))