class Solution:
    def reverseParentheses(self, s: str) -> str:
        # Stack + Recursion: O(n^2) time, O(n) space

        n = len(s)
        stack = []
        bracket_pair = {}
        for i, char in enumerate(s):
            if char == "(":
                stack.append(i)
            elif char == ")":
                bracket_pair[stack.pop()] = i

        def reverse_substring(start: int, end: int) -> str:
            substring = []
            i = start
            while i <= end:
                if s[i] == "(":
                    substring.append(
                        reverse_substring(i + 1, bracket_pair[i] - 1)[::-1]
                    )
                    i = bracket_pair[i] + 1
                else:
                    substring.append(s[i])
                    i += 1
            return "".join(substring)

        return reverse_substring(0, n - 1)
