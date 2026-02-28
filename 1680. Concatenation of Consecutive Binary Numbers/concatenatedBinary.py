class Solution:
    def concatenatedBinary(self, n: int) -> int:
        # Bit Manipulation: O(n * log(n)) time, O(1) space

        mod_factor = 10**9 + 7
        final_num = 0
        for num in range(1, n + 1):
            final_num = (final_num << num.bit_length() | num) % mod_factor
        return final_num
