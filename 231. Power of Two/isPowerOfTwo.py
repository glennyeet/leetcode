class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # Bit Manipulation: O(log(n)) time and O(1) space

        if n < 1:
            return False
        return n & 1 << n.bit_length() - 1 and n.bit_count() == 1
