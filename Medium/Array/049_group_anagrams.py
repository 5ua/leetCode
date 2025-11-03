from typing import List
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Dictionary to hold groups of anagrams
        groups = defaultdict(list)

        for word in strs:
            # Count frequency of each character ('a' to 'z')
            count = [0] * 26
            for char in word:
                count[ord(char) - ord('a')] += 1

            # Use tuple(count) as a unique signature for each anagram group
            groups[tuple(count)].append(word)

        # Return grouped anagrams
        return list(groups.values())
