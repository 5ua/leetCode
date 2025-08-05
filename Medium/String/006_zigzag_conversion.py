class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # Edge case: if only one row or numRows >= length of string,
        # no zigzag pattern is needed
        if numRows == 1 or numRows >= len(s):
            return s

        idx, d = 0, 1  # idx tracks current row, d is direction (1 = down, -1 = up)
        rows = [[] for _ in range(numRows)]  # Create a list of lists for each row

        # Place characters in appropriate rows following the zigzag pattern
        for char in s:
            rows[idx].append(char)
            # Change direction when reaching top or bottom row
            if idx == 0:
                d = 1  # Move down
            elif idx == numRows - 1:
                d = -1  # Move up
            idx += d  # Move to next row in current direction

        # Join characters in each row into strings
        for i in range(numRows):
            rows[i] = ''.join(rows[i])

        # Concatenate all rows into the final result
        return ''.join(rows)

solution = Solution()
print(solution.convert(s = "PAYPALISHIRING", numRows = 4))