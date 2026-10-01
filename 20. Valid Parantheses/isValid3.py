class Solution:
    def isValid(self, s: str) -> bool:
        # Stack: O(n) time, O(n) space

        stack = []
        bracket_pair = {"(": ")", "{": "}", "[": "]"}
        opening_brackets = list(bracket_pair.keys())
        for bracket in s:
            if (
                stack
                and stack[-1] in opening_brackets
                and bracket not in opening_brackets
            ):
                if bracket != bracket_pair[stack[-1]]:
                    return False
                else:
                    stack.pop()
            else:
                stack.append(bracket)
        if stack:
            return False
        return True
