from functools import cache


class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        # Top-down DP: O(z * o * l) time, O(z * o * l) space, where z is zero, o is one,
        # and l is limit

        mod_factor = 10**9 + 7

        @cache
        def count_stable_arrays(zeroes_left: int, ones_left: int, prev_bit: int):
            if zeroes_left == 0 and ones_left == 0:
                return 1
            count = 0
            if prev_bit != 0:
                for streak in range(1, min(limit + 1, zeroes_left + 1)):
                    count += count_stable_arrays(zeroes_left - streak, ones_left, 0)
            if prev_bit != 1:
                for streak in range(1, min(limit + 1, ones_left + 1)):
                    count += count_stable_arrays(zeroes_left, ones_left - streak, 1)
            return count % mod_factor

        return count_stable_arrays(zero, one, -1)
