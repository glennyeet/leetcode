from typing import List
from functools import cache


class Solution:
    def magicalSum(self, m: int, k: int, nums: List[int]) -> int:
        # Top-down DP: O(n * m^3 * k) time, O(n * m^2 * k) space

        n = len(nums)
        mod_factor = 10**9 + 7
        factorial = [1]
        inverse_factorial = [1]
        for i in range(1, m + 1):
            factorial.append(factorial[-1] * i % mod_factor)
            inverse_factorial.append(pow(factorial[-1], -1, mod_factor))

        @cache
        def sum_array_products(
            nums_index: int, seq_nums_left: int, set_bits_left: int, carry_bits: int
        ) -> int:
            if nums_index == n:
                if (
                    set_bits_left == 0
                    and seq_nums_left == 0
                    and carry_bits == 0
                    or carry_bits.bit_count() == set_bits_left
                    and seq_nums_left == 0
                ):
                    return 1
                return 0
            total = 0
            for i in range(seq_nums_left + 1):
                if set_bits_left >= (i + carry_bits) % 2:
                    total += (
                        sum_array_products(
                            nums_index + 1,
                            seq_nums_left - i,
                            set_bits_left - ((i + carry_bits) % 2),
                            (carry_bits + i) // 2,
                        )
                        * pow(nums[nums_index], i, mod_factor)
                        * inverse_factorial[i]
                    )
            return total

        return (sum_array_products(0, m, k, 0) * factorial[m]) % mod_factor
