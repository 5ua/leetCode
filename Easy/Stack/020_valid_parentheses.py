class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {'(': ')', '[': ']', '{': '}'}
        keys = brackets.keys()
        stack = []

        for i in range(len(s)):
            if s[i] in keys:
                stack.append(s[i])
            else:
                if not stack : return False
                if brackets[stack[-1]] == s[i] :
                    stack.pop()
                else: return False

        return len(stack) == 0


solution = Solution()
print(solution.isValid("]"))
###"([])"
