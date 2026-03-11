class Solution:
    def bitwiseComplement(self, n: int) -> int:
        # Big Manipulation: O(log(n)) time,
        # O(1) space

        if n == 0:
            return 1
        return n ^ 2 ** (n.bit_length()) - 1
