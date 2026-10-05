class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        # Stack: O(n) time, O(n) space, where n 
        # is the size of s

        stack = []
        for bracket in s:
            if bracket == "(":
                stack.append(-1)
            else:
                score = 0
                while stack and stack[-1] != -1:
                    score += stack.pop()
                stack.pop()
                if score == 0:
                    stack.append(1)
                else:
                    stack.append(2 * score)
        return sum(stack)
