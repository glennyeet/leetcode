from typing import List


class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        # Enumeration: O(n) time, O(1) space

        n = len(nums)
        sum_of_squares = 0
        for i in range(n):
            if n % (i + 1) == 0:
                sum_of_squares += nums[i] ** 2
        return sum_of_squares
