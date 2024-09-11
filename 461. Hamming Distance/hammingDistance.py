class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        # XOR
        dist = 0
        diff = x ^ y
        while diff:
            dist += diff & 1
            diff >>= 1
        return dist

        # Built-in function
        # return (x ^ y).bit_count()
