from math import gcd
from typing import List


class Solution:
    def findGCD(self, nums: List[int]) -> int:
        # Number Theory: O(n + log(m)) time,
        # O(1) space, where n is the size of
        # nums and m is the max value of nums

        return gcd(min(nums), max(nums))
