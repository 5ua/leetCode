from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        phone_map = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        output = []
        combination = []

        def backtrack(index: int):
            # If the combination is complete (same length as digits)
            if index == len(digits):
                output.append("".join(combination))
                return

            # Get possible letters for current digit
            letters = phone_map[digits[index]]
            for letter in letters:
                combination.append(letter)       # Choose
                backtrack(index + 1)             # Explore
                combination.pop()                # Un-choose (backtrack)

        backtrack(0)
        return output