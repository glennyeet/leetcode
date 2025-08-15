from math import log


class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        # Math: O(1) time, O(1) space

        if n <= 0:
            return False
        exponent = round(log(n, 4))
        return pow(4, exponent) == n
