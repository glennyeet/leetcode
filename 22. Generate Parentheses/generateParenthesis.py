from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # Backtracking: O(2^n) time, O(n) space

        combinations = []
        parantheses = []

        def generate_combinations(pairs_left: int, open_parantheses: int) -> None:
            if pairs_left == 0 and open_parantheses == 0:
                combinations.append("".join(parantheses))
                return
            if pairs_left > 0:
                parantheses.append("(")
                generate_combinations(pairs_left - 1, open_parantheses + 1)
                parantheses.pop()
            if open_parantheses > 0:
                parantheses.append(")")
                generate_combinations(pairs_left, open_parantheses - 1)
                parantheses.pop()

        generate_combinations(n, 0)
        return combinations
