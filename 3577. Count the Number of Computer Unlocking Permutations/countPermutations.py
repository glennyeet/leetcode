from typing import List
from math import factorial


class Solution:
    def countPermutations(self, complexity: List[int]) -> int:
        # Combinatorics: O(n) time, O(1) space

        n = len(complexity)
        mod_factor = 10**9 + 7
        for i, c in enumerate(complexity):
            if i > 0 and c <= complexity[0]:
                return 0
        return factorial(n - 1) % mod_factor
