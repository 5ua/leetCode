from typing import List
from collections import Counter, defaultdict

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        """
        Find all starting indices in s where the concatenation of all words appears exactly once
        and without any intervening characters.
        All words have the same length.
        """

        # Edge case: empty string or no words
        if not s or not words:
            return []

        word_len = len(words[0])
        word_count = len(words)
        total_len = word_len * word_count
        n = len(s)

        # Quick fail: if the total length of all words is larger than s
        if total_len > n:
            return []

        # Frequency map of given words
        target = Counter(words)
        result = []

        # We will slide windows starting from each offset in [0, word_len)
        for offset in range(word_len):
            left = offset                      # left boundary of the current window
            window = defaultdict(int)          # current window word frequencies
            words_used = 0                     # number of words currently in the window

            # Move right pointer in steps of word_len
            for right in range(offset, n - word_len + 1, word_len):
                curr_word = s[right:right + word_len]

                # If the current chunk is not a valid word, reset the window
                if curr_word not in target:
                    window.clear()
                    words_used = 0
                    left = right + word_len
                    continue

                # Include the current word in the window
                window[curr_word] += 1
                words_used += 1

                # If we used this word too many times, shrink from the left
                while window[curr_word] > target[curr_word]:
                    left_word = s[left:left + word_len]
                    window[left_word] -= 1
                    words_used -= 1
                    left += word_len

                # If we have exactly word_count words, check for a valid answer
                if words_used == word_count:
                    result.append(left)
                    # Optionally, we could move left and shrink by one word here
                    # to look for the next potential window:
                    # left_word = s[left:left + word_len]
                    # window[left_word] -= 1
                    # words_used -= 1
                    # left += word_len

        return result
