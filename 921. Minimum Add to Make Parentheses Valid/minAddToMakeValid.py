class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        for p in s:
            if len(stack) > 0 and stack[-1] == "(" and p == ")":
                stack.pop()
            else:
                stack.append(p)
        additions = len(stack)
        return additions
