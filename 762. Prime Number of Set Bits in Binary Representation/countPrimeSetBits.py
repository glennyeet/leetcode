from math import floor, sqrt


class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        # Bit Manipulation + Math: O(n * √b) time, O(1) space,
        # where n = right - left and b is the number of set bits
        # for any number in the range [left, right]

        prime_set_bit_nums = 0
        for num in range(left, right + 1):
            set_bits = num.bit_count()
            if set_bits <= 1:
                continue
            for factor in range(2, floor(sqrt(set_bits)) + 1):
                if set_bits % factor == 0:
                    break
            else:
                prime_set_bit_nums += 1
        return prime_set_bit_nums
