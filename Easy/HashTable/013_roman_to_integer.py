class Solution:
    def romanToInt(self, s: str) -> int:
        hmap = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        sum: int = 0
        for i in range(len(s)):
            if i < len(s)-1 and hmap[s[i]] < hmap[s[i + 1]]:
                sum -= hmap[s[i]]
            else:
                sum += hmap[s[i]]
        return sum


solution = Solution()
print(solution.romanToInt("MCMXCIV"))