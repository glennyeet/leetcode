class Solution:
    def checkValidString(self, s: str) -> bool:
        # Stack: O(n) time, O(n) space, where n
        # is the size of s

        open_brackets = []
        stars = []
        for i, bracket in enumerate(s):
            if bracket == "(":
                open_brackets.append(i)
            elif bracket == "*":
                stars.append(i)
            else:
                if open_brackets:
                    open_brackets.pop()
                elif stars:
                    stars.pop()
                else:
                    return False
        while open_brackets and stars:
            if open_brackets.pop() > stars.pop():
                return False
        return not open_brackets
