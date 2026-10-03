class Solution:
    def longestValidParentheses(self, s: str) -> int:
        # Stack: O(n) time, O(n) space

        max_substring_len = 0
        stack = []
        last_unmatched = -1
        for i, bracket in enumerate(s):
            if bracket == "(":
                stack.append(i)
            else:
                if stack:
                    stack.pop()
                    if not stack:
                        cur_substring_len = i - last_unmatched
                    else:
                        cur_substring_len = i - stack[-1]
                    max_substring_len = max(max_substring_len, cur_substring_len)
                else:
                    last_unmatched = i
        return max_substring_len
