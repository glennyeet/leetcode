from functools import cache
from math import ceil


class Solution:
    def soupServings(self, n: int) -> float:
        # Top-down DP: O(1) time, O(1) space

        @cache
        def calculate_probability(a_left: int, b_left: int) -> float:
            if a_left <= 0 and b_left <= 0:
                return 0.5
            elif a_left <= 0:
                return 1.0
            elif b_left <= 0:
                return 0.0
            return (
                calculate_probability(a_left - 4, b_left)
                + calculate_probability(a_left - 3, b_left - 1)
                + calculate_probability(a_left - 2, b_left - 2)
                + calculate_probability(a_left - 1, b_left - 3)
            ) / 4

        total_servings = ceil(n / 25)
        for i in range(1, total_servings + 1):
            if calculate_probability(i, i) > 1 - 1e-5:
                return 1.0
        return calculate_probability(total_servings, total_servings)
