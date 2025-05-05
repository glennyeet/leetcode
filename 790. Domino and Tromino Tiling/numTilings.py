from functools import cache


class Solution:
    def numTilings(self, n: int) -> int:
        # Top-down DP: O(n) time, O(n) space

        mod_factor = 10**9 + 7

        @cache
        def count_with_odd_ending(even_columns: int) -> int:
            if even_columns == 0:
                return 0
            count = count_with_even_ending(even_columns - 1) + count_with_odd_ending(
                even_columns - 1
            )
            return count % mod_factor

        @cache
        def count_with_even_ending(even_columns: int) -> int:
            if even_columns == 0:
                return 1
            count = count_with_even_ending(even_columns - 1)
            if even_columns - 2 >= 0:
                count += (
                    count_with_even_ending(even_columns - 2)
                    + count_with_odd_ending(even_columns - 2) * 2
                )
            return count % mod_factor

        return count_with_even_ending(n) % mod_factor
