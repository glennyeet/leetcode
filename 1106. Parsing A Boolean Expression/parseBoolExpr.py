class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        i = 0

        def solve_expression():
            nonlocal i
            if expression[i] == "t":
                i += 1
                return True
            elif expression[i] == "f":
                i += 1
                return False
            elif expression[i] == "!":
                i += 2
                evaluation = not solve_expression()
                i += 1
                return evaluation
            evaluations = []
            if expression[i] == "&":
                isAnd = True
            else:
                isAnd = False
            i += 2
            while expression[i] != ")":
                if expression[i] == ",":
                    i += 1
                else:
                    evaluations.append(solve_expression())
            i += 1
            if isAnd:
                return all(evaluations)
            else:
                return any(evaluations)

        return solve_expression()
