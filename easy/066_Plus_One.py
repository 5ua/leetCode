class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = 0
        for i in range(len(digits)):
            n = n * 10 + digits[i]

        str_n = list(str(n + 1))

        return [int(s) for s in str_n]