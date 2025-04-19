from typing import List
from bisect import bisect_left, bisect_right


class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        # Binary Search: O(nlog(n)) time, O(n) space, where n is the size of
        # nums

        sorted_nums = sorted(nums)

        # def binary_search(target: int, low: int, high: int) -> int:
        #     while low <= high:
        #         mid = low + (high - low) // 2
        #         if sorted_nums[mid] >= target:
        #             high = mid - 1
        #         else:
        #             low = mid + 1
        #     return high

        fair_pairs = 0
        for i, num in enumerate(sorted_nums):
            if num + sorted_nums[-1] < lower:
                continue
            elif num > upper // 2:
                break
            fair_pairs += bisect_right(sorted_nums, upper - num, i + 1) - bisect_left(
                sorted_nums, lower - num, i + 1
            )
        return fair_pairs
