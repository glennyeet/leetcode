from math import gcd, lcm
from typing import List


class Solution:
    def maxLength(self, nums: List[int]) -> int:
        # Enumeration + Math: O(n^3) time, O(n) space

        n = len(nums)
        max_subarray = 0
        for i in range(n):
            prod = 1
            for j in range(i, n):
                prod *= nums[j]
                if prod == lcm(*nums[i : j + 1]) * gcd(*nums[i : j + 1]):
                    max_subarray = max(max_subarray, j - i + 1)
        return max_subarray
