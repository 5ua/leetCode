class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        strArray = s.strip().split(" ")
        return len(strArray[-1])

        # for i, v in reversed(list(enumerate(s.split(' ')))):
        #     if v: return len(v)



solution = Solution()
print(solution.lengthOfLastWord("   fly me   to   the moon  "))