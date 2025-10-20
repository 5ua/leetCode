class Solution:
    def countAndSay(self, n: int) -> str:
        res = "1"  # Starting sequence
        for _ in range(n - 1):
            temp, i = "", 0
            # Iterate through the current sequence
            while i < len(res):
                count = 1
                # Count consecutive identical digits
                while i + 1 < len(res) and res[i] == res[i + 1]:
                    i += 1
                    count += 1
                # Append "count + digit" to the new string
                temp += str(count) + res[i]
                i += 1
            # Update the result for the next iteration
            res = temp
        return res
