class Solution:
    def countGoodNumbers(self, n: int) -> int:
        # Combinatorics: O(1) time, O(1) space

        mod_factor = 10**9 + 7
        odd_digits = n // 2
        even_digits = n - odd_digits
        return (
            pow(5, even_digits, mod_factor)
            * pow(4, odd_digits, mod_factor)
            % mod_factor
        )
