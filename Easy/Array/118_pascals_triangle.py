from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # Initialize Pascal's triangle with the first row
        result = [[1]]

        # Generate each row starting from the second row
        for i in range(1, numRows):
            prev_row = result[-1]
            new_row = [1]  # First element is always 1

            # Add elements between the first and last by summing adjacent elements from the previous row
            for j in range(len(prev_row) - 1):
                new_row.append(prev_row[j] + prev_row[j + 1])

            new_row.append(1)  # Last element is always 1
            result.append(new_row)

        return result


solution = Solution()
print(solution.generate(5))