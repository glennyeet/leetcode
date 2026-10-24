class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        # Dyck Path: O(n) time, O(n) space

        depth = 0
        res = []
        for bracket in s:
            if bracket == "(":
                if depth > 0:
                    res.append(bracket)
                depth += 1
            else:
                if depth > 1:
                    res.append(bracket)
                depth -= 1
        res = "".join(res)
        return res
