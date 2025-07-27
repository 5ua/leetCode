from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        # Start with the first row of Pascal's Triangle
        row = [1]

        # Build each row up to the desired index
        for _ in range(rowIndex):
            new_row = [1]  # First element is always 1

            # Add the sum of two adjacent elements from the previous row
            for j in range(1, len(row)):
                new_row.append(row[j - 1] + row[j])

            new_row.append(1)  # Last element is always 1
            row = new_row  # Update the row to the newly built one

        return row

solution = Solution()
print(solution.getRow(3))