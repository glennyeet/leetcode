from math import comb


class Solution:
    def countGoodArrays(self, n: int, m: int, k: int) -> int:
        # Combinatorics: O(1) time, O(1) space

        mod_factor = 10**9 + 7
        return m * pow(m - 1, n - 1 - k, mod_factor) * comb(n - 1, k) % mod_factor
