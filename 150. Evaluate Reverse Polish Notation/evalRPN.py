from typing import List
from math import trunc


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # Stack: O(n) time, O(n) space, where n
        # is the size of tokens

        stack = []
        operators = ("+", "-", "*", "/")
        for token in tokens:
            if token not in operators:
                stack.append(int(token))
            else:
                y = stack.pop()
                x = stack.pop()
                if token == "+":
                    stack.append(x + y)
                elif token == "-":
                    stack.append(x - y)
                elif token == "*":
                    stack.append(x * y)
                else:
                    stack.append(trunc(x / y))
        return stack[0]
