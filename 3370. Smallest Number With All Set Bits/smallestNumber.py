class Solution:
    def smallestNumber(self, n: int) -> int:
        x = 0
        for i in range(n.bit_length()):
            x |= 1 << i
        return x
