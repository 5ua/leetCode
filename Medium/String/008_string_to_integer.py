class Solution:
    def myAtoi(self, s: str) -> int:
        # 1. Remove leading whitespaces
        s = s.lstrip()
        if not s:
            return 0

        # 2. Initialize sign and starting index
        sign, i = 1, 0
        if s[0] == '-':
            sign = -1
            i += 1
        elif s[0] == '+':
            i += 1

        # 3. Constants for 32-bit signed integer limits
        INT_MIN, INT_MAX = -2**31, 2**31 - 1

        # 4. Convert characters to integer with overflow check
        num = 0
        while i < len(s) and s[i].isdigit():
            digit = ord(s[i]) - ord('0')  # Convert char to integer (0~9)

            # Check overflow BEFORE multiplying by 10 and adding digit
            if num > (INT_MAX - digit) // 10:
                return INT_MAX if sign == 1 else INT_MIN

            num = num * 10 + digit
            i += 1

        return sign * num
