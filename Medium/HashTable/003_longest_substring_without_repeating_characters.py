class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        max_length = 0  # Stores the length of the longest substring found
        char_set = set()  # Set to store unique characters in current window
        left = 0  # Left pointer of the sliding window

        for right in range(n):  # Right pointer expands the window
            # If current character is already in the set, shrink the window from the left
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1

            # Add the current character to the set
            char_set.add(s[right])

            # Update the maximum length if current window is longer
            max_length = max(max_length, right - left + 1)

        return max_length


solution = Solution()
print(solution.lengthOfLongestSubstring("pwwkew"))