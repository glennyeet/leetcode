from bisect import bisect_left, bisect_right
from math import floor


class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        sorted_nums = nums.copy()
        sorted_nums.sort()
        fair_pairs = 0
        for i, num in enumerate(sorted_nums):
            if num > floor(upper // 2):
                break
            fair_pairs += bisect_right(sorted_nums, upper - num, i + 1) - bisect_left(
                sorted_nums, lower - num, i + 1
            )
        return fair_pairs
