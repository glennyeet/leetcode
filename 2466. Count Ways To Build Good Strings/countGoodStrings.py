from functools import cache


class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        # Top-down DP: O(h) time, O(h) space, where h is high

        mod_factor = 10**9 + 7

        @cache
        def count_strings(string_len: int) -> int:
            good_strings = 0
            if string_len > high:
                return good_strings
            elif string_len >= low:
                good_strings += 1
            good_strings += count_strings(string_len + zero) + count_strings(
                string_len + one
            )
            good_strings %= mod_factor
            return good_strings

        return count_strings(0)
