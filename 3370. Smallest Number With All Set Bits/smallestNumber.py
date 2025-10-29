class Solution:
    def smallestNumber(self, n: int) -> int:
        # Bit Manipulation: O(log(n)) time,
        # O(1) space

        x = 0
        for i in range(n.bit_length()):
            x |= 1 << i
        return x
