from math import log


class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        # Math: O(1) time, O(1) space

        if n <= 0:
            return False
        exponent = round(log(n, 3))
        return pow(3, exponent) == n
