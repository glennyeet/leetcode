from math import gcd


class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        # Math: O(n) time, O(1) space

        sum_odd = 0
        sum_even = 0
        for i in range(1, n + 1):
            sum_odd += 2 * i - 1
            sum_even += 2 * i
        return gcd(sum_odd, sum_even)
