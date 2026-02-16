class Solution:
    def reverseBits(self, n: int) -> int:
        # Bit Manipulation: O(1) time, O(1) space

        reversed_num = 0
        for i in range(32):
            cur_bit = n >> i & 1
            reversed_num |= cur_bit << (31 - i)
        return reversed_num
