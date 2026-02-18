class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        # Bit Manipulation: O(1) time, O(1) space

        prev_bit = None
        cur_n = n
        while cur_n:
            cur_bit = cur_n & 1
            if prev_bit is not None and cur_bit == prev_bit:
                return False
            else:
                prev_bit = cur_bit
                cur_n >>= 1
        return True
