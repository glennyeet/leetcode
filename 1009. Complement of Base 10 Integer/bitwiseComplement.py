class Solution:
    def bitwiseComplement(self, n: int) -> int:
        if n == 0:
            return 1
        bits = 0
        n_copy = n
        while n_copy != 0:
            n_copy >>= 1
            bits += 1
        complement = n ^ (2**bits - 1)
        return complement
