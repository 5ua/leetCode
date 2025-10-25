class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # If either number is "0", the result is "0"
        if num1 == "0" or num2 == "0":
            return "0"

        # Result array to store intermediate sums
        res = [0] * (len(num1) + len(num2))

        # Reverse strings to make indexing easier
        num1 = num1[::-1]
        num2 = num2[::-1]

        # Multiply each digit
        for i in range(len(num1)):
            for j in range(len(num2)):
                # Convert char to digit and multiply
                product = (ord(num1[i]) - ord('0')) * (ord(num2[j]) - ord('0'))
                res[i + j] += product

                # Carry handling
                res[i + j + 1] += res[i + j] // 10
                res[i + j] %= 10

        # Convert list of digits back to string
        # Remove leading zeros at the end
        while res[-1] == 0:
            res.pop()

        # Reverse back to normal order
        return ''.join(map(str, res[::-1]))
