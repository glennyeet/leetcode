from typing import List
from collections import Counter


class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        # Hash Table: O(n) time, O(n) space, where n is the
        # size of nums

        frequency_counter = Counter(nums)
        most_common_nums = frequency_counter.most_common()
        max_frequency = most_common_nums[0][1]
        total_frequency = 0
        for _, frequency in most_common_nums:
            if frequency != max_frequency:
                break
            total_frequency += frequency
        return total_frequency
