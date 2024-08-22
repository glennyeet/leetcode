class Solution:
    def findComplement(self, num: int) -> int:
        bits = 0
        num_copy = num
        while num_copy != 0:
            num_copy >>= 1
            bits += 1
        complement = num ^ (2**bits - 1)
        return complement
