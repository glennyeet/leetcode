class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for b in s:
            if len(stack) > 0 and (
                stack[-1] == "("
                and b == ")"
                or stack[-1] == "{"
                and b == "}"
                or stack[-1] == "["
                and b == "]"
            ):
                stack.pop()
            else:
                stack.append(b)
        valid = len(stack) == 0
        return valid
