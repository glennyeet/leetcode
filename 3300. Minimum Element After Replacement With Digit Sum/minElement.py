from typing import List


class Solution:
    def minElement(self, nums: List[int]) -> int:
        # Array: O(n * log(n)) time, O(1) space, where
        # n is the size of nums

        min_digit_sum = float("inf")
        for num in nums:
            digit_sum = 0
            for digit in str(num):
                digit_sum += int(digit)
            min_digit_sum = min(min_digit_sum, digit_sum)
        return min_digit_sum
