from typing import *

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        INT_MAX, INT_MIN = 2**31 - 1, -2**31

        # Handle overflow case explicitly
        if dividend == INT_MIN and divisor == -1:
            return INT_MAX

        # Handle simple divisor = 1
        if divisor == 1:
            return dividend
        if divisor == -1:
            return -dividend

        # Determine the sign of the result
        sign = -1 if (dividend < 0) ^ (divisor < 0) else 1

        # Work with absolute values
        n, d = abs(dividend), abs(divisor)
        ans = 0

        # Subtract largest shifted divisor repeatedly
        while n >= d:
            p = 0
            while n >= (d << (p + 1)):
                p += 1
            n -= d << p
            ans += 1 << p

        # Apply sign and clamp to 32-bit range
        result = sign * ans
        return min(max(result, INT_MIN), INT_MAX)