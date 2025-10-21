from typing import List
from collections import Counter
from bisect import bisect_left, bisect_right


class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        # Hash Table + Binary Search: O(n * log(n)) time, O(n) space, where n is
        # the size of nums

        nums_counter = Counter(nums)
        sorted_nums = sorted(nums)
        max_frequency = 1
        for i in range(sorted_nums[0], sorted_nums[-1] + 1):
            left = bisect_left(sorted_nums, i - k)
            right = bisect_right(sorted_nums, i + k)
            max_frequency = max(
                max_frequency,
                nums_counter[i] + min(right - left - nums_counter[i], numOperations),
            )
        return max_frequency
