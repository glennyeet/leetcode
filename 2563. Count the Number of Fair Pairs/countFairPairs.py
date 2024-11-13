from bisect import bisect_left, bisect_right
from math import floor


class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        sorted_nums = nums.copy()
        sorted_nums.sort()

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
            elif num > floor(upper // 2):
                break
            # fair_pairs += binary_search(
            #     upper - num + 1, i + 1, len(sorted_nums) - 1
            # ) - binary_search(lower - num, i + 1, len(sorted_nums) - 1)
            fair_pairs += bisect_right(sorted_nums, upper - num, i + 1) - bisect_left(
                sorted_nums, lower - num, i + 1
            )
        return fair_pairs
