class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        # Backtracking: O(4^n / √n) time, O(4^n / √n) space

        combinations = []

        def generate(pairs_left: int, open_brackets: int, parentheses: str) -> None:
            if pairs_left == 0 and open_brackets == 0:
                combinations.append(parentheses)
                return
            if pairs_left > 0:
                generate(pairs_left - 1, open_brackets + 1, parentheses + "(")
            if open_brackets > 0:
                generate(pairs_left, open_brackets - 1, parentheses + ")")

        generate(n, 0, "")
        return combinations
