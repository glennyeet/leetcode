from typing import List


class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        # Enumeration: O(n^3) time, O(1) space

        n = len(nums)
        sum_of_squares = 0
        for i in range(n):
            for j in range(i, n):
                distinct_count = len(set(nums[i : j + 1]))
                sum_of_squares += distinct_count**2
        return sum_of_squares
