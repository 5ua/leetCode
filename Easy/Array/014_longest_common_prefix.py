from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        minStr = min(strs, key = lambda x : len(x))

        for i in range(len(minStr), 0, -1):
            prefix = minStr[:i]
            idx = 0
            for s in strs :
                idx += s.find(prefix)
                if idx != 0 : break
            if idx == 0 : return prefix

        return ''



solution = Solution()
print(solution.longestCommonPrefix(["bc","ca","c","aa"]))
#["dog", "racecar", "car"]
#"flower","flow","flight"