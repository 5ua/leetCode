class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand_around_center(left: int, right: int) -> str:
            # Expand as long as the characters match and are within bounds
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            # Return the palindrome substring
            return s[left+1:right]

        if len(s) <= 1:
            return s

        longest = ""

        for i in range(len(s)):
            # Odd-length palindrome (centered at i)
            p1 = expand_around_center(i, i)
            # Even-length palindrome (centered between i and i+1)
            p2 = expand_around_center(i, i + 1)

            # Update longest if a longer palindrome is found
            if len(p1) > len(longest):
                longest = p1
            if len(p2) > len(longest):
                longest = p2

        return longest

solution = Solution()
print(solution.longestPalindrome("babad"))