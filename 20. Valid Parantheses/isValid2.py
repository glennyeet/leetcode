class Solution:
    def isValid(self, s: str) -> bool:
        # Stack: O(n) time, O(n) space, where n is the size of s

        brackets_stack = []
        for bracket in s:
            if bracket == "(" or bracket == "{" or bracket == "[":
                brackets_stack.append(bracket)
            elif (
                not brackets_stack
                or bracket == ")"
                and brackets_stack[-1] != "("
                or bracket == "}"
                and brackets_stack[-1] != "{"
                or bracket == "]"
                and brackets_stack[-1] != "["
            ):
                return False
            else:
                brackets_stack.pop()
        return not brackets_stack
