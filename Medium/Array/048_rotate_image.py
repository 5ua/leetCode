from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Rotates the given n x n matrix by 90 degrees clockwise in-place.
        Approach:
        1. Reverse the matrix vertically.
        2. Transpose the matrix (swap across the main diagonal).
        """

        n = len(matrix)

        # Step 1: Reverse top and bottom rows (vertical flip)
        matrix.reverse()

        # Step 2: Transpose the matrix
        for i in range(n):
            for j in range(i + 1, n):
                # Swap elements across the main diagonal
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
